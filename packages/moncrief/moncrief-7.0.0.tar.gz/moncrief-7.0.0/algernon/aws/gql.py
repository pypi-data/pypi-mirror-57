import datetime
import hashlib
import hmac
import json
import os
import urllib.parse
from typing import Dict

import requests

from algernon.aws import operator


def _standardize_gql_endpoint(gql_endpoint: str):
    variable_fields = ('https://', 'http://', '/graphql')
    for field_name in variable_fields:
        gql_endpoint = gql_endpoint.replace(field_name, '')
    return gql_endpoint


class GqlSigner:
    _region = os.getenv('AWS_REGION', 'us-east-1')
    _service = 'appsync'

    def __init__(self, gql_endpoint: str):
        self._host = gql_endpoint
        self._uri = '/graphql'
        self._method = 'POST'
        self._signed_headers = 'host;x-amz-date'
        self._algorithm = 'AWS4-HMAC-SHA256'
        self._access_key = os.getenv('AWS_ACCESS_KEY_ID', None)
        self._secret_key = os.getenv('AWS_SECRET_ACCESS_KEY', None)
        self._session_token = os.getenv('AWS_SESSION_TOKEN', None)
        self._credentials = f"Credentials={self._access_key}"
        self._request_url = f'https://{gql_endpoint}{self._uri}'

    def generate_headers(self, query, variables):
        t = datetime.datetime.utcnow()
        amz_date = t.strftime('%Y%m%dT%H%M%SZ')
        date_stamp = t.strftime('%Y%m%d')
        canonical_request = self._generate_canonical_request(amz_date, query, variables)
        credential_scope = self._generate_scope(date_stamp)
        string_to_sign = self._generate_string_to_sign(canonical_request, amz_date, credential_scope)
        signature = self._generate_signature(string_to_sign, date_stamp)
        headers = self._generate_headers(credential_scope, signature, amz_date)
        return headers

    def _generate_canonical_request(self, amz_date, query, variables):
        payload = {'query': query, 'variables': variables}
        canonical_headers = f'host:{self._host}\nx-amz-date:{amz_date}\n'
        payload_hash = hashlib.sha256(json.dumps(payload).encode('utf-8')).hexdigest()
        canonical_request = f"{self._method}\n{self._uri}\n\n{canonical_headers}\n{self._signed_headers}\n{payload_hash}"
        return canonical_request

    def _generate_string_to_sign(self, canonical_request, amz_date, scope):
        hash_request = hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()
        return f"{self._algorithm}\n{amz_date}\n{scope}\n{hash_request}"

    def _generate_scope(self, date_stamp):
        return f"{date_stamp}/{self._region}/{self._service}/aws4_request"

    def _get_signature_key(self, date_stamp):
        k_date = self._sign(f'AWS4{self._secret_key}'.encode('utf-8'), date_stamp)
        k_region = self._sign(k_date, self._region)
        k_service = self._sign(k_region, self._service)
        k_signing = self._sign(k_service, 'aws4_request')
        return k_signing

    def _generate_signature(self, string_to_sign, date_stamp):
        signing_key = self._get_signature_key(date_stamp)
        signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()
        return signature

    def _generate_headers(self, credential_scope, signature, amz_date):
        credentials_entry = f'Credential={self._access_key}/{credential_scope}'
        headers_entry = f'SignedHeaders={self._signed_headers}'
        signature_entry = f'Signature={signature}'
        authorization_header = f"{self._algorithm} {credentials_entry}, {headers_entry}, {signature_entry}"
        headers = {
            'x-amz-date': amz_date,
            'Authorization': authorization_header,
            'Content-Type': "application/graphql"}
        if self._session_token:
            headers['X-Amz-Security-Token'] = self._session_token
        return headers

    @classmethod
    def _generate_request_parameters(cls, command):
        payload = {'gremlin': command}
        request_parameters = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
        payload_hash = hashlib.sha256(''.encode('utf-8')).hexdigest()
        return payload_hash, request_parameters

    @classmethod
    def _sign(cls, key, message):
        return hmac.new(key, message.encode('utf-8'), hashlib.sha256).digest()


class GqlDriver:
    _region = os.getenv('AWS_REGION', 'us-east-1')
    _service = 'appsync'

    def __init__(self, gql_endpoint: str, session: requests.session() = None):
        if not session:
            session = requests.session()
        self._session = session
        self._gql_endpoint = gql_endpoint
        self._uri = '/graphql'
        self._request_url = f'https://{gql_endpoint}{self._uri}'

    @classmethod
    def build(cls, api_name, session: requests.session() = None):
        endpoint = operator.lookup_resource(api_name)
        gql_endpoint = _standardize_gql_endpoint(endpoint)
        return cls(gql_endpoint, session)

    def send(self, command: str, variables: Dict = None):
        if not variables:
            variables = {}
        signer = GqlSigner(self._gql_endpoint)
        headers = signer.generate_headers(command, variables)
        payload = {'query': command, 'variables': variables}
        if os.getenv('DEBUG', 'False') == 'True':
            headers = {'x-api-key': os.environ['GQL_API_KEY']}
        response = requests.post(self._request_url, headers=headers, json=payload)
        if response.status_code != 200:
            raise RuntimeError(f'error communicating with GQL API: {response.text}, '
                               f'command: {command}, variables: {variables}')
        return response.text
