def optimize(matrix):
    durations = matrix["durations"]

    tour = [0]
    remaining_sights = list(range(1, len(durations)))

    for i in range(len(remaining_sights)):
        last_sight = tour[-1]
        shortest_duration = 0
        next_sight = 0

        for sight in remaining_sights:
            duration = durations[last_sight][sight]
            print(duration)

            if shortest_duration == 0 or duration < shortest_duration:
                shortest_duration = duration
                next_sight = sight

        tour.append(next_sight)
        remaining_sights.remove(next_sight)

    return tour
