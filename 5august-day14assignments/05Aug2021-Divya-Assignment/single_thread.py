import threading
def print_no():
    for i in range(1,10):
        print(i)
t1=threading.Thread(target=print_no)     #create thread
t1.start()
t1.join()
print(".............")
