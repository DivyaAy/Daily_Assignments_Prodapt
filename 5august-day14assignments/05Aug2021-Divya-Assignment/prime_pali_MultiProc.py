import multiprocessing,logging
start = 2
end = 10
def primeProcess(start,end):
    for n in range(start,end+1):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                print("the prime numbers are:",n)
def paliProcess(start,end):
    for l in range(start,end+1):
        temp=l
        reverse =0
        while(temp>0):
            p=temp%10
            reverse = (reverse*10)+p
            temp=temp//10
        if(l==reverse):
            print("The palindrome numbers are:",l)
if __name__=='__main__':
    try:
        p1 = multiprocessing.Process(target=primeProcess,args=(start,end,))
        p2 = multiprocessing.Process(target=paliProcess,args=(start,end,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print("...........")
    except:
        logging.error("something went wrong")
    finally:
        print("Good Job")

