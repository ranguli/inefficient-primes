import time 


class algorithms:

    class iterative1:
        # The initial naive solution. It consists of finding a prime number
        # then immediately writing it to the csv.

        def __init__(self, i, datafile):
            self.i = i
            self.datafile = datafile

        def isPrime(self, i):
            prime = True
            for j in range(2, i):
                if (i % j == 0):
                    prime = False
            return prime

        def generateAllPrimes(self, i, datafile):
            startTime = time.time()
            f = open(self.datafile, "w")
            for j in range(self.i):
                if self.isPrime(j):
                    executionTime = int(time.time() - startTime)
                    f.write(str(j) + "," + str(executionTime) + "\n")
            f.close()

    class iterative2:
        # Currently does the exact same thing as iterative1. This will
        # eventually become a different algorithm.

        def __init__(self, i, datafile):
            self.i = i
            self.datafile = datafile

        def isPrime(self, i):
            prime = True
            for j in range(2, i):
                if (i % j == 0):
                    prime = False
                    time.sleep(0.05)
            return prime

        def generateAllPrimes(self, i, datafile):
            startTime = time.time()
            f = open(self.datafile, "w")
            for j in range(self.i):
                if self.isPrime(j):
                    executionTime = int(time.time() - startTime)
                    f.write(str(j) + "," + str(executionTime) + "\n")
            f.close()
