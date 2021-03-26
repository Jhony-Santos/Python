
from multiprocessing import process
import threading
import time
import random

def minhathread(n):
    t = random.randint(1,3)
    global count
    time.sleep(t)
    count+=1
    print("Thread {0} depois de {1}s\n".format(n, t))

inicio=time.time()
count=0
threads=[]
for i in range(10):
    t=threading.Thread(target=minhathread, args=(i,))
    threads.append(t)
    t.start()

for x in threads:
    x.join()

print("Threads que acordaram ", count)
print("tempo decorrido ", time.time()-inicio)


