import time, csv, sys
from numexpr import cpuinfo

from algorithms import *

assert sys.version_info >= (3,0)
import matplotlib.pyplot as plt


def main():
  
    i = int(input("Enter a number to generate primes below it: "))
    algorithm1 = algorithms.iterative1(i, "algorithm1_results.csv")
    algorithm1.generateAllPrimes(i, "algorithm1_results.csv")

    algorithm2 = algorithms.iterative2(i, "algorithm2_results.csv")
    algorithm2.generateAllPrimes(i, "algorithm2_results.csv")
    
    Plot.plot("algorithm1_results.csv")
    Plot.plot("algorithm2_results.csv")
    Plot.graph()        

class Plot:

    def plot(datafile): 

        # Frankly, I didn't care to learn matplotlib this time around.
        # This code is from:
        # https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/
  
        x = []
        y = []
        cpu = cpuinfo.cpu.info[0]['model name']

        with open(datafile, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                x.append(int(row[0]))
                y.append(int(row[1]))
    
        plt.plot(x, y, label = "algorithm1(" + cpu + ")")

    def graph():
        plt.xlabel('Prime Number')
        plt.ylabel('Execution Time')
        plt.title("Prime Number Generation over Execution Time")
        plt.legend()
        plt.show()

main()




