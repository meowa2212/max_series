'''
Wojciech Gorzynski
28-03-2025 v2
Searches for longest algebraic series of primes.
Changes:
    -uses multithreading
'''

import multiprocessing
import os

# Function to check if a number is prime
def isPrime(n):
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

def lesserPrime(n): # returns the first lesser prime number returns -1 if none is found
    if n > 2:
        for i in range(1, n-1):
            potentialPrime = n-i
            if isPrime(potentialPrime):
                return potentialPrime
    return -1

def lesserPrimes(n): # returns a list of all the lesser primes
    primes = []
    lesser = lesserPrime(n)
    while lesser != -1:
        primes.append(lesser)
        lesser = lesserPrime(lesser)
    return primes

def primorial(n): # returns the primorial returns -1 if there is none
    if isPrime(n):
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
    while isPrime(b+difference):
        length += 1
        b += difference
    return length

def generateSeries(a, difference, length): # returns a series in a list
    series = [a,]
    for i in range(length-1):
        series.append(a+difference)
        a += difference
    return series

# Worker function for each process
def seriesFinder(start, step, depthNonPrime, k):
    a = start
    generateLength = k
    while True:
        if isPrime(a):
            multiple = 1
            while depthNonPrime >= multiple: 
                difference = primorial(k)*multiple
                b = a+difference
                if isPrime(b):
                    length = checkSeries(a,b)
                    if length >= generateLength:
                        print(f"{generateSeries(a, difference, generateLength)} r:{difference} l:{length}")
                multiple += 1
        a += step

if __name__ == "__main__":
    print("doesn't find the minimal series for k < 8")
    k = int(input("target length of a series: "))
    depthNonPrime = int(input("depth of the search algorhytm: "))
    
    # Number of processes
    numProcesses = int(input("number of processes (defaults to number of CPU cores): ") or os.cpu_count())
    processes = []

    # Start processes on distinct ranges of odd numbers
    for i in range(numProcesses):
        process = multiprocessing.Process(target=seriesFinder, args=(3 + i * 2, numProcesses * 2, depthNonPrime, k))
        processes.append(process)
        process.start()

    # Print the first prime manually (since it's 2 and all processes start with odd numbers)
    a = 2
    generateLength = k
    multiple = 1
    while depthNonPrime >= multiple: 
        difference = primorial(k)*multiple
        b = a+difference
        if isPrime(b):
            length = checkSeries(a,b)
            if length >= generateLength:
                print(f"{generateSeries(a, difference, generateLength)} r:{difference} l:{length}")
        multiple += 1

    # Wait for all processes to finish
    for process in processes:
        process.join()
