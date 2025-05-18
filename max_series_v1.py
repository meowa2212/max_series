'''
Wojciech Gorzynski
27-03-2025 v1
Searches for longest algebraic series of primes.
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

def primesList(n):  # generates the starting search pool of n+1 amount of primes
    primesList = [2,]
    while len(primesList) <= n:
        nextPrime = primesList[len(primesList)-1]+1
        while not isPrime(nextPrime):
            nextPrime += 1
        primesList.append(nextPrime)
    return primesList

def primeShift(listPrimes): # shifts the list of primes by one element
    listPrimes.pop(0)
    nextPrime = listPrimes[len(listPrimes)-1]+2
    while not isPrime(nextPrime):
        nextPrime += 2
    listPrimes.append(nextPrime)

def checkSeries(a,b): # uses the first two values of a series to calculate it's length
    difference = b-a
    length = 2
    while isPrime(b+difference):
        length += 1
        b += difference
    return length

def generateSeries(a, difference, length):
    series = [a,]
    for i in range(length-1):
        series.append(a+difference)
        a += difference
    return series

def main(): # main function
    depth = int(input("The depth of the search algorythm: ")) # the range of the search algorhytm
    target = int(input("Select the looked after length (-1 if just the longest found): "))
    listPrimes = primesList(depth) # algorhytm initialization

    if target == -1:
        maxLength = 3
        maxStart = 0
        maxDifference = 0 

        while True: # the algorhytm (patented)
            startElement = listPrimes[0]
            for secondElement in listPrimes[1::]:
                newLength = checkSeries(startElement, secondElement)
                if newLength >= maxLength:
                    maxLength = newLength
                    maxStart = startElement
                    maxDifference = secondElement - startElement
                    print(f"{generateSeries(maxStart, maxDifference, maxLength)} r: {maxDifference} l: {maxLength}")
            primeShift(listPrimes)
    else:
        while True: # the algorhytm (patented)
            startElement = listPrimes[0]
            for secondElement in listPrimes[1::]:
                newLength = checkSeries(startElement, secondElement)
                if newLength >= target:
                    difference = secondElement - startElement
                    print(f"{generateSeries(startElement, difference, target)} r: {difference} l: {newLength}")
            primeShift(listPrimes)


if __name__ == "__main__":
    main()