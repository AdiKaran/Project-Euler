# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def SeiveEratosthenes(n):

    prime_factors = [True for i in range(n)]
    prime_factors[0] = prime_factors[1] = False 

    for i in range( len(prime_factors)):

        if prime_factors[i] == True :
            if n % i == 0:
                yield i
            for x in range(i*i, n, i):
                prime_factors[x] = False
             

def PrimeFactor(n):
    print( [x for x in SeiveEratosthenes(n)] )
   
PrimeFactors(600851475143)