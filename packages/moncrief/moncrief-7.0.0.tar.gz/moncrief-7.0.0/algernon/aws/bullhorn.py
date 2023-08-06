from queue import Queue
from threading import Thread
from typing import Dict

import boto3

from algernon.aws import operator


class Bullhorn:
    def __init__(self, topic_map: Dict[str, str], client=None, num_batch_threads: int = 25):
        if not client:
            client = boto3.client('sns')
        self._client = client
        self._topic_map = topic_map
        self._num_threads = num_batch_threads
        self._batch_mode = False

    def __enter__(self):
        self._workers = []
        self._batch = Queue()
        self._batch_mode = True
        for _ in range(self._num_threads):
            worker = Thread(target=self._batch_publish)
            worker.start()
            self._workers.append(worker)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type and not exc_val:
            self._shutdown_workers()
            self._workers = []
            self._batch_mode = False
            return True
        raise (exc_type(exc_val))

    @classmethod
    def retrieve(cls, profile=None, num_batch_threads: int = 25):
        topic_map = {}
        client = boto3.client('sns')
        if profile:
            client = boto3.Session(profile_name=profile).client('sns')
        return cls(topic_map, client, num_batch_threads=num_batch_threads)

    @property
    def topic_map(self):
        return self._topic_map

    def _shutdown_workers(self):
        for _ in self._workers:
            self._batch.put(None)
        for worker in self._workers:
            worker.join()

    def find_task_arn(self,  task_name):
        if task_name not in self._topic_map:
            task_arn = operator.lookup_resource(task_name)
            self._topic_map[task_name] = task_arn
        return self._topic_map.get(task_name)

    def publish(self, message_subject: str, topic_arn: str, message_body: str):
        if self._batch_mode:
            self._batch.put({
                "Subject": message_subject,
                "TopicArn": topic_arn,
                "Message": message_body
            })
            return
        response = self._client.publish(
            TopicArn=topic_arn,
            Subject=message_subject,
            Message=message_body
        )
        return response['MessageId']

    def _batch_publish(self):
        client = boto3.client('sns')
        while True:
            order = self._batch.get()
            if order is None:
                return
            client.publish(**order)
            self._batch.task_done()
