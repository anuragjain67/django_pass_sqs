import unittest
from cuegg.taskqueue import MultiProcessQueue

def say_hello(params):
    from time import sleep
    sleep(10) # Sleep for 10s, just to prove that the task is in fact running in the background
    
    if 'name' in params:
        name = params['name']
    else:
        name = "Anonymous"
    print "Hello, %s" % name

class TestMultiProcessQueue(unittest.TestCase):
    def test_multiprocess_queue(self):
        task_map = {"greet": say_hello}
        taskqueue = MultiProcessQueue(task_map)
        taskqueue.add("greet", {"name": "Sripathi"})
        print "Task Queued"
        from time import sleep
        sleep(15) # Sleep for 15s, to give the worker thread a chance to finish

class TestSqsTaskQueue(unittest.TestCase):
    def test_add(self):
        pass