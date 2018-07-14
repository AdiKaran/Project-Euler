

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

#Todo: Brute force method is working alright... However finding the palindromes first and factorizing them after should improve the speed for larger inputs


def IsPalindrome(intx):
    if str(intx)==str(intx)[::-1]: return True
    else: return False
    
palindrome_factors = []*2
largest_pal = 0
pals = []
    
for i in range(1000):
    for j in range(i+1,1000):
        product = i * j
        if product > largest_pal and IsPalindrome(product):
            largest_pal = product


print(largest_pal)







