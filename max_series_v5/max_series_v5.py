'''
Wojciech Gorzynski
10-09-2025 v5
Searches for longest algebraic series of primes.
Changes:
    -choice to use traditional algorithm instead Miller-Rabin primality test
    -aproximates the depth of the search algorhytm
    -uses sieve of eratosthenes to generate the primorial
'''

import multiprocessing
import os
import math

# optional function to check if a number is prime
def isPrime_any(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

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
def seriesFinder(start, step, k):
    a = start
    generateLength = k
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
                    if length >= generateLength:
                        print(f"{generateSeries(a, difference, generateLength)} l:{length}, d:{depthNonPrime}")
                multiple += 1
        a += step


if __name__ == "__main__":
    print("doesn't find the minimal series for k < 8")
    k = int(input("target length of a series: "))
    
    choice = input("use Miller-Rabin primality test? (Y/n): ")
    if choice == '' or choice.lower() == 'y':
        from Miller_Rabin_test import isPrime_any

    
    # Number of processes
    numProcesses = int(input("number of processes (defaults to number of CPU cores): ") or os.cpu_count())
    processes = []


    # Start processes on distinct ranges of odd numbers
    for i in range(numProcesses):
        process = multiprocessing.Process(target=seriesFinder, args=(3 + i * 2, numProcesses * 2, k))
        processes.append(process)
        process.start()

    # Print the first prime manually (since it's 2 and all processes start with odd numbers)
    a = 2
    generateLength = k 
    multiple = 1
    depthNonPrime = math.ceil(max(20, 10*math.log(max(1, k*a/50000))))
    primorialVal = primorial(k)
    while depthNonPrime >= multiple: 
        difference = primorialVal*multiple
        b = a+difference
        if isPrime_any(b):
            length = checkSeries(a,b)
            if length >= generateLength:
                print(f"{generateSeries(a, difference, generateLength)} l:{length}, d:{depthNonPrime}")
        multiple += 1

    # Wait for all processes to finish
    for process in processes:
        process.join()
