# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

max =100
def SeiveEratosthenes(n):

    primes = [True for i in range(n)]
    primes[0] = primes[1] = False 

    for i in range( len(primes)):

        if primes[i] == True :
            yield i
            for x in range(i*i, n, i):
                primes[x] = False
    
    return primes 
             

def Sum(in_list):
    sum = 0
    for x in in_list:
        sum += x
    return sum

    
print(Sum(SeiveEratosthenes(2000000)))