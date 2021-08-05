import multiprocessing
def square(getlist):
    for i in getlist:
        print(i*i)
def cube(getlist):
    for i in getlist:
        print(i*i*i)
if(__name__)=='__main__':
    mylist=[2,3,4,5]
    p1=multiprocessing.Process(target=square,args=(mylist,))
    p2=multiprocessing.Process(target=cube,args=(mylist,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("............")
