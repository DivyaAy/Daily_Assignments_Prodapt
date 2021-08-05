import threading
def printHello():
    for i in range(5):
        print("hello")
def printl():
    for j in range(5):
        print("divya")
t1 = threading.Thread(target=printHello)
t2 = threading.Thread(target=printl)
t1.start()
t2.start()
t1.join()
t2.join()
print("FInished")