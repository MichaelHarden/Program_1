from Driving_data import cities 
from random import random 
import statistics
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

def hundred_k_standard_deviation():
    '''
    This function makes a list (hundred_k_list) and stores the 100,000 drives
    and returns the standard deviation of the list
    @Param: None
    @return: statistics.stdev(hundred_k_list) this is the standard deviation of the list hundred_k_list
    '''
    hundred_k_list = list()
    for _ in range(100_000):
        hundred_k_list.append(drive())
    return statistics.stdev(hundred_k_list)

def ten_k_standard_deviation():
    '''This function stores the 10,000 trips into a list and returns the 
    standard deviation of the list
    @Param: None
    @returns: statistics.stdev(ten_k) this is the standard deviation of the list ten_k
    '''
    ten_k = list()
    for _ in range(10_000):
        ten_k.append(drive())
    return statistics.stdev(ten_k)


ten_ten_thousand_runs_list_avg = list()#for the ten iterations of the ten thousand drives
for _ in range(10):
    ten_ten_thousand_runs_list_avg.append(ten_k())#puts all the average in a list



print(f"the average distance that was travled over 10,000 trips is:  {ten_k()}")
print(f"the standard deviation that was travled over 10,000 trips is:  {ten_k_standard_deviation()}")
print("\n")
print(f"the average distance that was travled over 10 iterations of 10,000 trips is: {ten_iter}")
print(f"the average of the averages distance that was travled over 10 iterations of 10,000 trips is: {sum(ten_ten_thousand_runs_list_avg) / len(ten_ten_thousand_runs_list_avg)}") # average of the averages
print(f"the standard deviation of the average that was travled over 10 iterations of 10,000 trips is: {statistics.stdev(ten_ten_thousand_runs_list_avg)} ")
print("\n")
print(f"the average distance that was travled over 100,000 trips is is:  {hundred_k()}")
print(f"the standard deviation that was travled over 100,000 trips is is:  {hundred_k_standard_deviation()}")

