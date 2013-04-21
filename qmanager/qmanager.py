#-*- coding: utf-8 -*-
import Queue
from multiprocessing.managers import BaseManager, BaseProxy


class NRTQueueManager(BaseManager):
    def __init__(self, address=('localhost', 50000,), authkey=''):
        super(NRTQueueManager, self).__init__(address, authkey)
        self.register('NRTQueue', callable=lambda: _NRT_queue, proxytype=NRTQueueProxy,
                      exposed=('__len__','put','get', 'size', 'clear', 'task_done'))

class NRTQueueProxy(BaseProxy):
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


class NRTQueue(Queue.Queue):
    def clear(self):
        with self.mutex:
            self.queue.clear()

    def __len__(self):
        return self.qsize()

_NRT_queue = NRTQueue()

class NRTQueueServer(object):
    def run(self):
        self.manager = NRTQueueManager()
        self.manager.get_server().serve_forever()

    def shutdown(self):
        self.manager.shutdown()


if __name__ == '__main__':
    server = NRTQueueServer()
    server.run()
