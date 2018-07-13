

#Seive of Eratosthenes
max =100
def SeiveEratosthenes(n):

    primes = [True for i in range(n)]
    primes[0] = primes[1] = False 

    for i in range( len(primes)):

        if primes[i] == True :
            yield i
            for x in range(i*i, n, i):
                primes[x] = False
             

def Primes_under_n(n):
    print( [x for x in SeiveEratosthenes(n)] )
   
Primes_under_n(10000000)



        










