#-*- coding: utf-8 -*-
import Queue
from multiprocessing.managers import BaseManager, BaseProxy


class QueueManager(BaseManager):
    def __init__(self, address=('localhost', 50000,), authkey=''):
        super(QueueManager, self).__init__(address, authkey)
        self.register('NRTQueue', callable=lambda: _queue, proxytype=QueueProxy,
                      exposed=('__len__','put','get', 'size', 'clear', 'task_done'))

class QueueProxy(BaseProxy):
    def put(self, data):
        return self._callmethod('put', args=(data,))

    def get(self):
        return self._callmethod('get')

    def size(self):
        return self._callmethod('__len__')

    def clear(self):
        return self._callmethod('clear')

    def task_done(self):
        return self._callmethod('task_done')

    def __len__(self):
        return self._callmethod('__len__')


class Queue(Queue.Queue):
    def clear(self):
        with self.mutex:
            self.queue.clear()

    def __len__(self):
        return self.qsize()

_queue = Queue()

class QueueServer(object):
    def run(self):
        self.manager = QueueManager()
        self.manager.get_server().serve_forever()

    def shutdown(self):
        self.manager.shutdown()


if __name__ == '__main__':
    server = QueueServer()
    server.run()
