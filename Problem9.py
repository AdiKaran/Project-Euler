

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2

# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


sqr_roots = {}
ans = [] * 3

for x in range(500) :
    sqr_roots[x**2] = x

a = 1
b =1
while a < 1000:
    for b in range(1,a):
        hypotenuse = a ** 2 + b **2 
        
        try:
            c = sqr_roots[hypotenuse]
            
            if a + b + c == 1000:
                print('[a,b,c,hypotenuse,abc] =',a,b,c,hypotenuse,a*b*c)
        except KeyError:
            pass
       
    a += 1
       
                 