
# # Shor’s quantum algorithm
import math
import gmpy2
import time

N = int(input("Enter N: ")) 
a = int(input("Enter a: ")) 

print("===============================================") 

# test it for 3 * 5 = 15 , 2693 * 2699 = 7268407

g = math.gcd(a, N) 

r, x = 1, pow(a, 1, N)

while x != 1: 
    r, x = r+1, pow(a, r, N)

y = pow(a, r//2, N)

print(math.gcd(y-1,N), math.gcd(y+1,N))
 
print("===============================================")


for i in range(2, int(math.sqrt(N))+1):
    if N % i == 0:
        print(i, N // i)

print("===============================================") 