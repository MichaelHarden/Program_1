from Cities import cities 
from random import random 


def drive():
    distance_traveled = 0
    current_city = cities['A']
    while current_city != cities['P']:
        choice = random()
        neighboring_cities = current_city['neighbors']  
        if choice <= current_city[neighboring_cities[0]]['prob']:
            distance_traveled += current_city[neighboring_cities[0]]['distance']
            current_city = cities[neighboring_cities[0]]
        else:
            distance_traveled += current_city[neighboring_cities[1]]['distance']
            current_city = cities[neighboring_cities[1]]
    return distance_traveled




def ten_k(): return sum(drive() for _ in range(10_000))/10_000

def hundred_k(): return sum(drive() for _ in range(100_000))/100_000

ten_iter = sum(ten_k() for _ in range(10))/10


print(f"the average distance that was travled over 10,000 trips is is:  {ten_k()}")
print(f"the average distance that was travled over 10 iterations of 10,000 trips is is: {ten_iter}")
print(f"the average distance that was travled over 100,000 trips is is:  {hundred_k()}")

