import time
import matplotlib.pyplot as plt
import csv


outputFile = "primes.csv"

x = []
y = []

def isPrime(i):
    prime = True 
    for j in range(2, i):
        if (i % j == 0):
            prime = False
    return prime 

def generateAllPrimes(i, outputFile):
    startTime = time.time()
    f = open(filename, "w")
    for j in range(i):
        if isPrime(j):
            executionTime = round(time.time() - startTime, 3)
            f.write(str(j) + "," + str(executionTime) + "\n") 
    f.close() 

def main():
    i = int(input("Enter a number to generate primes below it:"))
    startTime = time.time() 
    primes = generateAllPrimes(i)
    if (isPrime(i)):
        print(str(i) + " itself is a prime number") 
    else:
        print(str(i) + " itself is not a prime number.")

    print("It took " + str(round(time.time() - startTime, 2) ) + " seconds to generate primes below it.")
    print("The results have been save to \"primes.txt\"")

def plotTime(inputFile):
   
    # Frankly, I didn't care to learn matplotlib this time around.
    # This code is from: 
    # https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/

    x = []
    y = []
  
    with open(inputfile, 'r') as csvfile:
        plots = csv.reader(csvfile,delimiter=',')
        for row in plots:
        x.append(int[rows[0]))
        y.append(int[rows[1]))
    plt.plot(x,y label='Loaded from file!')
    plt.xlabel('Prime Number')
    plt.ylaber('Execution Time')
    plt.tiel("Prime Number Generation over Execution Time")
    plt.legend()
    plt.show()

main() 
plotTime()

