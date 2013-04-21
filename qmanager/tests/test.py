#-*- coding: utf-8 -*-
import unittest
from qmanager import qmanager


class ClassTest(unittest.TestCase):
    def test_put(self):
        client = qmanager.NRTQueueManager()
        client.connect()
        queue = client.NRTQueue()
        queue.clear()
        queue.put('test')

        self.assertEqual(queue.size(), 1)
        queue.task_done()

    def test_get(self):
        client = qmanager.NRTQueueManager()
        client.connect()
        queue = client.NRTQueue()
        queue.clear()
        queue.put('test')
        element = queue.get()

        self.assertEqual(element, 'test')
        queue.task_done()


if __name__ == '__main__':
    unittest.main()
