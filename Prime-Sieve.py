# 0. Here, Prime = True(1) & Not_Prime/Composite = False(0)
# 1. Opt. Sieve = Simple Sieve + Odd No. + Root n(Segmented) + i^2
# 2. App. of Sieve : Prime No. Series Gen. (U/L Limit)
# 3. App. of Sieve : Prime factor of 'n' (Shortest Prime Factor/SPF)
# 4. App. of Sieve : "Nth" Prime No.

# math lib for sqrt function in case of future imp.
import math

def PrintList(num_list,n):
    # Optimize print Function - Future imp.
    for i in range(n+1):
        if num_list[i]:
            print(i)
            
def SieveOfEratosthenes(n):
    # Optimization - Below list will make 0,1 and Odd No. False
    num_list=[False if i==0 or i==1 or (i>2 and i%2==0) else True for i in range(n+1) ]
    # print(math.sqrt(n)) or int(n ** 0.5) + 1
    # Optmzn. - loop from 3 to sqrt(n) with multiples of nested i^2
    for i in range(3, int(n ** 0.5)+1, 2):
        if(num_list[i]==True):
            j = 0
            for j in range(i*i, n+1,j+i):
            	num_list[j] = False
    PrintList(num_list,n)
            
def Prime_Num_Series(z):
    SieveOfEratosthenes(z)

def PrimeFactor_Sieve(n):
    while n%2 == 0: 
        print(2) 
        n=n/2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n%i== 0: 
            print(i)
            n=n/i 
    if n>2: 
        print(n)

def counter(num_list,n):
    counter = 0
    for i in range(n+1):
        if num_list[i]:
            counter+=1
    return counter
    
def N_Prime_Num(y):
    n = 2*y
    count = 0
    num_list=[False if i==0 or i==1 or (i>2 and i%2==0) else True for i in range(n+1)]
    for i in range(3, int(n ** 0.5)+1, 2):
        if(num_list[i]==True):
            j = 0
            for j in range(i*i, n+1,j+i):
            	num_list[j] = False
    count = counter(num_list,n)
    return count,num_list,y

if __name__ == '__main__':
    n = 10
    x = 315
    z = 20
    y = 12
    print("=============== Sieve of Eratosthenes ===============")
    print("The Prime Numbers upto "+str(n)+" are : ")
    SieveOfEratosthenes(n)
    
    print("=============== Prime Factors of N (WRONG) ==================")
    print("The Prime Factors of "+str(x)+" are : ")
    PrimeFactor_Sieve(x)
    
    print("=============== Prime No. Series Upto N =============")
    print("The Prime No. Series Upto "+str(z)+" are : ")
    Prime_Num_Series(z)
    
    print("=============== Nth Prime No. =======================")
    count = 0
    m = y
    count, num_list,y = N_Prime_Num(y)
    while(count<=y):
        count, num_list,m = N_Prime_Num(count+m)
        count+=m
    final_list = []
    for i,val in enumerate(num_list):
        if val:
            final_list.append(i)
    print("The "+str(y)+"th Prime No. is : "+str(final_list[y-1]))