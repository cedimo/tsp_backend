import gurobipy as gp
from gurobipy import GRB
from itertools import combinations

# Callback - use lazy constraints to eliminate sub-tours
def subtourelim(model, where):
    if where == GRB.Callback.MIPSOL:
        # make a list of edges selected in the solution
        vals = model.cbGetSolution(model._vars)
        selected = gp.tuplelist((i, j) for i, j in model._vars.keys() if vals[i, j] > 0.5)
        # find the shortest cycle in the selected edge list
        tour = subtour(selected)
        if len(tour) < n:
            # add subtour elimination constr. for every pair of cities in tour
            model.cbLazy(gp.quicksum(model._vars[i, j] for i, j in combinations(tour, 2)) <= len(tour)-1)

# Given a tuplelist of edges, find the shortest subtour
def subtour(edges):
    unvisited = list(range(n))
    cycle = range(n+1)  # initial length has 1 more city
    while unvisited:  # true if list is non-empty
        thiscycle = []
        neighbors = unvisited
        while neighbors:
            current = neighbors[0]
            thiscycle.append(current)
            unvisited.remove(current)
            neighbors = [j for i, j in edges.select(current, '*') if j in unvisited]
        if len(cycle) > len(thiscycle):
            cycle = thiscycle
    return cycle



def optimize(matrix):
    durations = matrix["durations"]
    
    global n
    n = len(durations)

    durations_dict = {(i, j):
        durations[i][j]
        for i in range(n) for j in range(i)}

    # GUROBI
    m = gp.Model()

    vars = m.addVars(durations_dict.keys(), obj=durations_dict, vtype=GRB.BINARY)
    for i, j in vars.keys():
        vars[j, i] = vars[i, j]

    m.addConstrs(vars.sum(i, '*') == 2 for i in range(n))

    # Optimize model

    m._vars = vars
    m.Params.lazyConstraints = 1
    m.optimize(subtourelim)

    vals = m.getAttr('x', vars)
    selected = gp.tuplelist((i, j) for i, j in vals.keys() if vals[i, j] > 0.5)

    tour = subtour(selected)
    assert len(tour) == n

    return tour