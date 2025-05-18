'''
Wojciech Gorzynski
28-03-2025 v2
Searches for longest algebraic series of primes.
Changes:
-uses the ap-k primorial principle
 for calculating the common difference of non prime lengthed series
'''

def isPrime(n): # checks if a number is prime
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def lesserPrime(n): # returns the first lesser prime number returns -1 if none is found
    if n > 2:
        for i in range(1, n-1):
            potentialPrime = n-i
            if isPrime(potentialPrime):
                return potentialPrime
    return -1

def nextPrime(n): # returns the next prime number
    if n != 2:
        n += 2
    else:
        n += 1
    while True:
        if isPrime(n):
            return n
        n += 2

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

def main(): # main function
    print("doesn't find the minimal series for k < 8")
    k = int(input("target length of a series: "))
    depthNonPrime = int(input("depth of the search algorhytm: "))
    generateLength = k
    print("starts")
    a = 2
    while True:
        multiple = 1
        while depthNonPrime >= multiple: 
            difference = primorial(k)*multiple
            b = a+difference
            if isPrime(b):
                length = checkSeries(a,b)
                if length >= generateLength:
                    print(f"{generateSeries(a, difference, generateLength)} r:{difference} l:{length}")
            multiple += 1
        a = nextPrime(a)

if __name__ == "__main__":
    main()