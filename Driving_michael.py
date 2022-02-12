from Driving_data import cities
from random import random
import numpy as np

def drive():
    """
    drive generages a random path between the cities 'A' to 'P', following the
    provided probabilites. Then, returns the distance traveled over that path.
    """
    dist_traveled = 0   # tracks the distance traveled
    current_city = cities['A']      # tracks the current city
    while current_city != cities['P']: # loops unitl the city P is reached
        choice = random()
        neighboring_cities = current_city['neighbors']

        # if the chosen random number is less than the smaller probabilistic
        # neighbor, then that is the next city. Otherwise the larger
        # probabilistic neighbor is the next city.
        #
        # the distance which is required to travel from the current city to
        # the next city is added to dist_traveled. and current_city is added
        # to dist_traveled
        if choice <= current_city[neighboring_cities[0]]['prob']:
            dist_traveled += current_city[neighboring_cities[0]]['distance']
            current_city = cities[neighboring_cities[0]]
        else:
            dist_traveled += current_city[neighboring_cities[1]]['distance']
            current_city = cities[neighboring_cities[1]]
    return dist_traveled

def n_drives(n):
    """
    calculates average driving distance and standard deviation over n drives.
    this information is then returned as a tuple.

    Parameters:
        n: number of drives

    Return:
        tuple()
            [0]: the average driving distance of n runs
            [1]: standard deviation over those n runs.
    """
    drive_times = [drive() for _ in range(n)]
    std_dev = np.std(drive_times)
    avg_drive_dist = np.average(drive_times)
    return (avg_drive_dist, std_dev)


trip = n_drives(10_000)
print(f"""the average distance that was travled over 10,000 trips is :  {trip[0]}
and the standard deviation is {trip[1]}\n""")

trip = n_drives(100_000)
print(f"""the average distance that was travled over 10,000 trips is :  {trip[0]}
and the standard deviation is {trip[1]}\n""")


# calculates the average of 10 iterations of the average distance over 10,000 runs
ten_iter_trips = [n_drives(10_000) for _ in range(10)]
it = []
ten_iter = (
    # averaging the averages of each iteration
    sum(avg_dist[0] for avg_dist in ten_iter_trips)/10,
    # averaging the standard deviation of each iteration
    sum(avg_dist[1] for avg_dist in ten_iter_trips)/10
)

print(f"""the average of the average distance that was travled over 10, 10,000 trip iterations is :  {ten_iter[0]}
and the average standard deviation is {ten_iter[1]}\n""")
