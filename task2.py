# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

from xmlrpc.client import boolean


def eratosthenes(n):
    primes = []
    limit = n
    sieve = []
    for i in range(limit + 1):
        sieve.append(True)
    a = 2
    while a ** 2 <= limit:
        if sieve[a] == True:
            for b in range(a ** 2, limit + 1, a):
                sieve[b] = False
        a += 1
    for a in range(2, limit + 1):
        if sieve[a] == True:
            primes.append(a)
    return primes

def factorize(x):
    primes = eratosthenes(x)
    factors = []
    while x != 1:
        for i in primes:
            if x % i == 0:
                factors.append(i)
                x = x / i
                break 
    return factors

n = int(input("Please input N: "))
print (factorize(n))
