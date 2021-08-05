import logging
import threading
lower = 2
upper = 10
def primeNum(lower,upper):
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print("the prime numbers are:",num)

      
def palindrome(lower,upper):
    for j in range(lower,upper+1):
        temp=j
        reverse =0
        while(temp>0):
            p=temp%10
            reverse = (reverse*10)+p
            temp=temp//10
        if(j==reverse):
            print("The palindrome numbers are:",j)
try:
    t1=threading.Thread(target=primeNum,args=(lower,upper,))
    t2=threading.Thread(target=palindrome,args=(lower,upper,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("............")
except:
    logging.error("something went wrong")
finally:
    print("Good Job")