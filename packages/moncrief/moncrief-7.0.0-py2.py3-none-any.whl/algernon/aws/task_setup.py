import uuid

import boto3
import rapidjson

from algernon.aws import Bullhorn, StoredData
from algernon.serializers import AlgJson


def _generate_callback(current_task_name: str, callback: str):
    if not callback:
        return None, False
    chain_links = callback.split('#')
    if len(chain_links) == 1:
        return callback, False
    if current_task_name not in chain_links:
        return chain_links[0], True
    for pointer, link in enumerate(chain_links):
        if link == current_task_name:
            try:
                return chain_links[pointer+1], True
            except IndexError:
                return None, False


def _callback(original_payload, bullhorn=None, result=None, ):
    callback_fn, chained = _generate_callback(original_payload['task_name'], original_payload.get('callback'))
    if not callback_fn:
        return bullhorn
    if bullhorn is None:
        bullhorn = Bullhorn.retrieve()
    topic_arn = bullhorn.find_task_arn(callback_fn)
    if result is None:
        result = {}
    if result:
        result = StoredData.from_object(uuid.uuid4(), result, full_unpack=True)
    msg = {'task_name': callback_fn, 'task_kwargs': result}
    if chained:
        msg['callback'] = original_payload.get('callback')
    bullhorn.publish('callback', topic_arn, AlgJson.dumps(msg))
    return bullhorn


def _mark_state_machine_event_success(task_token, results):
    client = boto3.client('stepfunctions')
    client.send_task_success(
        taskToken=task_token,
        output=AlgJson.dumps(results)
    )


def _mark_state_machine_event_failed(task_token, error, cause=None):
    client = boto3.client('stepfunctions')
    kwargs = {
        'taskToken': task_token,
        'error': AlgJson.dumps(error)
    }
    if cause:
        kwargs['cause'] = AlgJson.dumps(cause)
    client.send_task_failure(**kwargs)


def _run_state_machine_event(production_fn, event, context):
    input_args = rapidjson.loads(event['Input'])
    task_token = event['TaskToken']
    try:
        results = production_fn(input_args, context)
        _mark_state_machine_event_success(task_token, results)
    except Exception as e:
        _mark_state_machine_event_failed(task_token, e.args)


def rebuild_event(original_event):
    return AlgJson.loads(AlgJson.dumps(original_event))


def queued(preserve=False):
    def wrap(production_fn):
        def wrapper(*args):
            results = []
            event = args[0]
            bullhorn = None
            local_context = {'lambda': args[1]}
            for entry in event['Records']:
                local_context['sqs'] = {
                    'message_id': entry['messageId'],
                    'receipt_handle': entry['receiptHandle'],
                    'source_arn': entry['eventSourceARN'],
                    'aws_region': entry['awsRegion']
                }
                entry_body = rapidjson.loads(entry['body'])
                original_payload = rapidjson.loads(entry_body['Message'])
                if "Input" in original_payload and "TaskToken" in original_payload:
                    _run_state_machine_event(production_fn, original_payload, local_context)
                    continue
                try:
                    result = production_fn(original_payload, local_context)
                    results.append(result)
                    bullhorn = _callback(original_payload, bullhorn, result)
                except PipelineTerminationException as e:
                    result = AlgJson.dumps(e.terminal_results)
                    results.append(result)
            if preserve:
                raise RuntimeError('do not let AWS delete the messages we just processed')
            return results
        return wrapper
    return wrap


def stated(production_fn):
    def wrapper(*args):
        event = args[0]
        sfn_context = event.get('sfn_context', {})
        task_kwargs = event.get('payload', {})
        if task_kwargs:
            task_kwargs = rapidjson.loads(task_kwargs)
        local_context = {'lambda': args[1], 'sfn': sfn_context}
        task_name = event.get('task_name')
        if not task_name:
            state_context = sfn_context.get('State', {})
            task_name = state_context.get('Name', {})
        if not task_kwargs:
            task_kwargs = {x: y for x, y in event.items() if x not in ['task_name', 'sfn_context', 'payload']}
        rebuilt_event = {'task_name': task_name, 'task_kwargs': task_kwargs}
        result = production_fn(rebuilt_event, local_context)
        return AlgJson.dumps(result)

    return wrapper


class PipelineTerminationException(Exception):
    def __init__(self, terminal_results):
        self._terminal_results = terminal_results

    @property
    def terminal_results(self):
        return self._terminal_results
