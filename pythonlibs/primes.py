import primesieve
import random
import math
import sympy
import os


class Primes:

    def next_prime(p):
        print(primesieve.nth_prime(p))

    # return the first n primes

    def primes(n):
        p = []
        for i in range(n):
            p.append((primesieve.nth_prime(i)))
        return p

    # return all primer between a and b
    def primes_range(a, b):
        p = []
        for i in range(a, b):
            p.append((primesieve.nth_prime(i)))
        return p

    def generateLargePrime(k):
        # k is the desired bit length
        r = 100*(math.log(k, 2)+1)  # number of attempts max
        r_ = r
        while r > 0:
            # randrange is mersenne twister and is completely deterministic
            # unusable for serious crypto purposes
            n = random.randrange(2**(k-1), 2**(k))
            r -= 1
            if sympy.isprime(n) == True:
                return n

        return 0  # f"Error: Failure after {r_} tries."

    def getRandomPrime(file='primes.txt'):
        cwd = os.getcwd()
        with open(f"{cwd}/pythonlibs/{file}", "r") as f:
            lines = f.readlines()

        p = random.choice(lines)
        if p == '\n':
            p = random.choice(lines)

        return int(p)


#p = Primes.primes_range(1000,1100)
for i in range(1000):
    p = Primes.generateLargePrime(1024)
    if(p != 0):
        print(p)

# file = "primes.txt"
# p = Primes.getRandomPrime()
# print(p)
