import multiprocessing
def even(getlist):
    for i in getlist:
        if i%2==0:
            print("the even numbers are:",i)
        else:
            print("nothing")
def odd(getlist):
    for j in getlist:
        if j%2==1:
            print("the odd numbers are: ",j)
if (__name__)=='__main__':
    list= [1,2,3,4,5,6]
    p1=multiprocessing.Process(target=even,args=(list,))
    p2=multiprocessing.Process(target=odd,args=(list,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("..........")