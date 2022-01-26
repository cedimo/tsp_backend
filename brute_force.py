from  itertools import permutations

def brute_force(matrix):
    durations = matrix["durations"]
    places_count = len(durations)

    # alle möglichen Anordnungen der Punkte außer 0
    # 0 bleibt immer Start- und Endpunkt 
    possible_routes = list(permutations(range(1, places_count), places_count-1))
    
    shortest_duration = 0
    shortest_route = 0

    for possible_route in possible_routes:
        # duration von 0 zu erstem Punkt
        duration = durations[0][possible_route[0]]

        for i in range(len(possible_route)):
            if i+1 < len(possible_route):
                duration += durations[possible_route[i]][possible_route[i+1]]
            else:
                duration += durations[possible_route[i]][0]
        

        if shortest_duration == 0 or duration < shortest_duration:
            shortest_duration = duration
            shortest_route = possible_route

    tour = [0]
    for x in shortest_route:
        tour.append(x)

    return tour