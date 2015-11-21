import threading
import time

class Thread (threading.Thread):
    #construtor da thread devera inicializar os atributos da thread e do IA
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    #metodo chamado ao iniciar a thread nele será chamado 
    def run(self):
        # Get lock to synchronize threads
        threadLock.acquire()
        #executa IA(parametros...)
        # Free lock to release next thread
        threadLock.release()

threadLock = threading.Lock()#responsavel para organizar os acessos de cada thread
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1")
thread2 = myThread(2, "Thread-2")

# Start new Threads
thread1.start()#ira executar o metodo sobrescrito run()
thread2.start()

# Add threads to thread list  
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"