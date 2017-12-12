# task_master.py

import random, time
import queue
from multiprocessing.managers import BaseManager
#
task_queue = queue.Queue()
#
result_queue = queue.Queue()

#
class QueueManager(BaseManager):
    pass

#
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# QueueManager.register('get_map_queue', callable=lambda: map_queue)
#
manager = QueueManager(address=('', 5000), authkey=b'abc')
#
manager.start()
#
task = manager.get_task_queue()
result = manager.get_result_queue()
#
n = 1
for i in range(10):
    print('Put task %d...' % n)
    task.put(n)
    n = n+1
#
print('Try get results...')
for i in range(10):
    r = result.get(timeout=1000)
    print('Code complexity result: \n %s' % r)
#
manager.shutdown()
print('master exit.')