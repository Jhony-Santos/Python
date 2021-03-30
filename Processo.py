
from multiprocessing import process
import time
import random

#processo= o espaço de memória é independente.
def meuprocesso(n):
    global count
    t=random.randint(1,3)
    time.sleep(t)
    count+=1
    print("Processo {0} depois de {1}s\n".format(n,t))


count=0
if __name__== '__main__':
    inicio=time.time()
    count=0
    processes=[ ]
    for i in range(10):
        t=Process(target=meuprocesso,args=(i,))
        processes.append(t)
        t.start()
    for x in processes:
        x.join()

print("Processos que acordaram ",count)
print("Tempo decorrido ", time.time()-inicio)