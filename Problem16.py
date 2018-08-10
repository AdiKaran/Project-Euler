
# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000

num = 2**1000
num_str = str(num)

print(sum(int(x) for x in num_str))
