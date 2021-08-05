import threading
def square(getlist):
    for i in getlist:
        print(i*i)
def cube(getlist):
    for i in getlist:
        print(i*i*i)
mylist=[2,3,4,5]
t1=threading.Thread(target=square,args=(mylist,))
t2=threading.Thread(target=cube,args=(mylist,))
t1.start()
t2.start()
t1.join()
t2.join()
print("............")
