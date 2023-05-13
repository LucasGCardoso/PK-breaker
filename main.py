import sys
import random
from math import gcd as gcd
import time


def is_prime(num):
  for i in range(2,num):
    if (num%i) == 0:
      return False
  return True


if len(sys.argv) <= 1:
    print("Usage: python prime_factor N")
    print("Where N is a multiplication of two prime numbers.")
    exit()
n = int(sys.argv[1])
if(is_prime(n)):
    print("The number N should not be a prime. Instead, it should be a multiplication of two primes.")
    exit()
MAX_ITERATIONS = 10
print(f"Trying to find the two possible primes that factor {n}. This may take a while.")
iteration = 0
start_time = time.time()
while True:
    while True:
        g = random.SystemRandom().randint(2,n-1)
        if gcd(n, g) == 1:
            break

    for r in range(1, n):
        remainder = (g**r)%n
        if remainder == 1:
            break

    possible_factor_sharing_x = g**(r//2) + 1
    possible_factor_sharing_y = g**(r//2) - 1

    p = gcd(possible_factor_sharing_x, n)
    q = gcd(possible_factor_sharing_y, n)

    if p * q == n and is_prime(p) and is_prime(q):
        print(f"The two possible primes that factor {n} are: ")
        print("P: ", p)
        print("Q: ", q)
        print(f"Program took {iteration} iterations.")
        print("--- Executed in %s seconds ---" % (time.time() - start_time))
        exit()
    else:
        iteration+=1
        if iteration == MAX_ITERATIONS:
            print(f"Program exited after {iteration} iterations")
            break
        continue

print("I am sorry, we could not find the two correct factors. What a shame :(")
print("--- Executed in %s seconds ---" % (time.time() - start_time))
