'''
Wojciech Gorzynski
10-09-2025 v5
Searches for longest algebraic series of primes.
Changes:
    -aproximates the depth of the search algorhytm WIP
    -uses sieve of eratosthenes to generate the primorial
    -cleaned up the code
'''

import multiprocessing
import os
import math

from Miller_Rabin_test import isPrime_any

def lesserPrimes(n): # returns a list of all the lesser primes
    if n < 2:
        return []
    primes = [2]  # Include 2 manually
    sieve_size = (n - 1) // 2  # only odd numbers > 2
    sieve = [True] * sieve_size

    for i in range(int(n**0.5)//2 + 1):
        if sieve[i]:
            p = 2*i + 3  # actual prime number
            # start marking from p*p
            start_idx = (p*p - 3)//2
            for j in range(start_idx, sieve_size, p):
                sieve[j] = False

    # collect primes
    primes.extend([2*i + 3 for i, is_prime in enumerate(sieve) if is_prime])
    return primes

def primorial(n): # returns the primorial returns -1 if there is none
    if isPrime_any(n):
        primes = [n,]
        primes.extend(lesserPrimes(n))
    else:
        primes = lesserPrimes(n)
    if len(primes) == 0:
        return -1
    primorialVal = primes[0]
    for prime in primes[1::]:
        primorialVal *= prime
    return primorialVal

def checkSeries(a,b): # calculates a series length
    difference = b-a
    length = 2
    while isPrime_any(b+difference):
        length += 1
        b += difference
    return length

def generateSeries(a, difference, length): # returns a series in a list
    series = [a + i*difference for i in range(length)]
    return series

# Worker function for each process
def seriesFinder(a, step, k):
    primorialVal = primorial(k)
    while True:
        if isPrime_any(a):
            multiple = 1
            depthNonPrime = math.ceil(max(20, 10*math.log(max(1, k*a/50000))))
            while depthNonPrime >= multiple: 
                difference = primorialVal*multiple
                b = a+difference
                if isPrime_any(b):
                    length = checkSeries(a,b)
                    if length >= k:
                        print(f"{generateSeries(a, difference, k)} len:{length}, dth:{depthNonPrime}, dif:{difference}")
                multiple += 1
        a += step

def main():
    print("doesn't find the minimal series for k < 8")
    k = int(input("target length of a series: "))
    
    # Number of processes
    numProcesses = int(input(f"number of processes (defaults to: {os.cpu_count()}): ") or os.cpu_count())
    processes = []

    # Start processes on distinct ranges of odd numbers
    for i in range(numProcesses):
        process = multiprocessing.Process(target=seriesFinder, args=(3 + i * 2, numProcesses * 2, k))
        processes.append(process)
        process.start()


if __name__ == "__main__":
    main()