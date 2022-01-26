import os
import sys
from time import time

def solve(matrix, algorithm, *optional_algorithms):
    for x in optional_algorithms:
        solve_and_print(matrix, x)

    return solve_and_print(matrix, algorithm, True)


def solve_and_print(matrix, algorithm, shown=False):
    # block print (because of gurobi)
    sys.stdout = open(os.devnull, 'w')

    start = time()
    tour = algorithm.optimize(matrix)
    end = time()

    # enable print
    sys.stdout = sys.__stdout__

    print("")
    if shown:
        print("SHOWN IN FRONTEND")
    print("----- " + str(algorithm.__name__) +" -----")
    print("duration: " + str(end-start) + "s")
    print("tour: " + str(tour))
    print("")

    return tour