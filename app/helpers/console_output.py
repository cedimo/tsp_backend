import os
import sys
from time import time
from app.helpers.openrouteservice import getRoute

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

    route = getRoute(matrix, tour)
    x = route.json()['features'][0]['properties']['summary']
    distance = round(x['distance'])
    duration = round(x['duration']/60)

    # enable print
    sys.stdout = sys.__stdout__

    if shown:
        print("SHOWN IN FRONTEND")
    print(f"----- {algorithm.__name__} -----")
    print(f"calculation duration: {end-start} s")
    print(f"tour: {tour}")
    print(f"tour distance: {distance} m")
    print(f"tour duration: {duration} min")
    print("")

    return tour