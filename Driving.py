from Driving_data import cities 
from random import random 

# drive generages a random path between the cities 'A' to 'P' and returns the
# distance traveled over that path.
def drive():
    dist_traveled = 0   # tracks the distance taken to the current city
    current_city = cities['A']      # tracks the city
    while current_city != cities['P']: # loops unitl the city p is reached
        choice = random()   
        neighboring_cities = current_city['neighbors']  

        # if the random number choosen is less than the smaller probabilistic 
        # neighbor, then that is the next city. Otherwise the larger
        # probabilistic neighbor is choosen as the next city. 
        #
        # the distance which is required to travel from the current city to
        # the next city is added to dist_traveled.
        if choice <= current_city[neighboring_cities[0]]['prob']:
            dist_traveled += current_city[neighboring_cities[0]]['distance']
            current_city = cities[neighboring_cities[0]]
        else:
            dist_traveled += current_city[neighboring_cities[1]]['distance']
            current_city = cities[neighboring_cities[1]]
    return dist_traveled



# calculates average driving dsitance over 10,000 drives
def ten_k(): return sum(drive() for _ in range(10_000))/10_000

# calculates the average distance driven over 100,000 drives
def hundred_k(): return sum(drive() for _ in range(100_000))/100_000

# calculates the average of 10 iterations of the average distance over 10,000 runs
ten_iter = sum(ten_k() for _ in range(10))/10


print(f"the average distance that was travled over 10,000 trips is is:  {ten_k()}")
print(f"the average distance that was travled over 10 iterations of 10,000 trips is is: {ten_iter}")
print(f"the average distance that was travled over 100,000 trips is is:  {hundred_k()}")

