# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Fundamental Theorem of Arithmetic:
    # Every integer i>=2 can be expressed as a rpoduct of prime numbers




def PrimeFactors(num):
    p = 2
    FactList = []
    while p * p <= num:
        
        if num % p == 0 :
            
            num = num // p
          
            FactList.append(p)

        elif p == 2:
            p =3
        
        else :
            p += 2
    if num > p : 
        FactList.append(num)

    return FactList

def List_Prime_Factors(integer):

    print([ x for x in PrimeFactors(integer)])


List_Prime_Factors(600851475143)


