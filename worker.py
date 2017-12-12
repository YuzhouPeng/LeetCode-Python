# task_worker.py

import time, sys, queue
import os,re
from multiprocessing.managers import BaseManager

#
class QueueManager(BaseManager):
    pass

#
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

###  task number
taskNum = int(input('enter the taskNum :  '))
###


#
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
#
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
#
m.connect()
#
task = m.get_task_queue()
result = m.get_result_queue()
#
for i in range(taskNum):
    try:

        n = task.get(timeout=1)
        stringn = str(n)
        filen = "radon cc -a testfiles/"+stringn+'.py'
        r = os.popen(filen)
        text = r.read()
        r.close()
        print (text)
        pat = "Average complexity: \w \((\d+(\.\d+)?)\)"
        number = re.findall(pat, text)[0]
        r = number[0]
        r = 'file %d: %s' % (n,r)
        # r = int(r)
        print('run task %d ...' % n )
        print ("returning  result.......\n")
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')

#
print('worker exit.')