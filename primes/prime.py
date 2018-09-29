import time, csv, sys
assert sys.version_info >= (3,0)

import matplotlib.pyplot as plt



datafile = "primes.csv"

x = []
y = []


def isPrime(i):
    prime = True
    for j in range(2, i):
        if (i % j == 0):
            prime = False
    return prime


def generateAllPrimes(i, datafile):
    startTime = time.time()
    f = open(datafile, "w")
    for j in range(i):
        if isPrime(j):
            executionTime = int(time.time() - startTime)
            f.write(str(j) + "," + str(executionTime) + "\n")
    f.close()


def main(datafile):
    i = int(input("Enter a number to generate primes below it: "))
    startTime = time.time()
    primes = generateAllPrimes(i, datafile)
    if (isPrime(i)):
        print(str(i) + " itself is a prime number,", end='')
    else:
        print(str(i) + " itself is not a prime number,", end='')

    print(" and it took " + str(round(time.time() - startTime, 2)) +
          " seconds to figure that out.")
    print("*The results have been save to " + str(datafile) + "*" )
    print("Your number is " + str(23249425 - i) + " less than the highest prime number ever discovered.")


def plotTime(datafile):

    # Frankly, I didn't care to learn matplotlib this time around.
    # This code is from:
    # https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/

    x = []
    y = []

    with open(datafile, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))
    plt.plot(x, y, label = 'Iterative Generation')
    plt.xlabel('Prime Number')
    plt.ylabel('Execution Time')
    plt.title("Prime Number Generation over Execution Time")
    plt.legend()
    plt.show()


main(datafile)
plotTime(datafile)
