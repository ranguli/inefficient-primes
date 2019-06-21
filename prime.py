import time
import csv
import sys
import os

from numexpr import cpuinfo
import matplotlib.pyplot as plt

assert sys.version_info >= (3,0)

class Algorithms:

    class Iterative:

        # The initial naive solutions. They consists of finding a prime number
        # and immediately writing it to the csv.

        class SolutionA:

            def __init__(self, i, datafile):
                self.i = i
                self.datafile = datafile

            def isPrime(self, i):
                prime = True
                for j in range(2, i):
                    if (i % j == 0):
                        prime = False
                return prime

            def generate_primes(self):
                startTime = time.time()
                f = open(self.datafile, "w+")
                for j in range(self.i):
                    if self.isPrime(j):
                        executionTime = int(time.time() - startTime)
                        f.write(str(j) + "," + str(executionTime) + "\n")
                f.close()
        
        class SolutionB:
            
            # The same as Solution A, but we open and close the .csv 
            # for each result just to make them look different on the
            # graph.
            # (not an actual solution)

            def __init__(self, i, datafile):
                self.i = i
                self.datafile = datafile

            def isPrime(self, i):
                prime = True
                for j in range(2, i):
                    if (i % j == 0):
                        prime = False
                return prime

            def generate_primes(self):
                os.remove(self.datafile)
                startTime = time.time()
                for j in range(self.i):
                    f = open(self.datafile, "a+")
                    if self.isPrime(j):
                        executionTime = int(time.time() - startTime)
                        f.write(str(j) + "," + str(executionTime) + "\n")
                    f.close()

class Plot:

    def plot_csv(datafile, title): 

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
        
        title = title + " " + " ".join(cpuinfo.cpu.info[0]['model name'].split())

        plt.plot(x, y, label=title)

    def graph():
        plt.xlabel('Prime Number')
        plt.ylabel('Execution Time')
        plt.title("Prime Number Generation over Execution Time")
        plt.legend()
        plt.show()

def main():
    
    datafile_algorithm_a = "algorithm_a_results.csv" 
    datafile_algorithm_b = "algorithm_b_results.csv" 
  
    i = int(input("Enter a number to generate all of the primes less than it: "))
    
    algorithm_a = Algorithms.Iterative.SolutionA(i, datafile_algorithm_a)
    algorithm_a.generate_primes()

    algorithm_b = Algorithms.Iterative.SolutionB(i, datafile_algorithm_b)
    algorithm_b.generate_primes()
    
    Plot.plot_csv(datafile_algorithm_a, "Minimum amount of file open/close")
    Plot.plot_csv(datafile_algorithm_b, "Lots of unecessary file open/close")
    Plot.graph()        

main()

