# First, import random function

from random import random

# Now, define necessary functions.

# My driving simulation is 
# going to be a recursion-based
# approach. I will have a function
# called distToPFrom(start) which
# takes in string representing the
# start town.
# distToPFrom will simulate a random
# distance from start to P by 
# determining which next town the car
# goes to, and adding the distance 
# from start to nextTown to the 
# distance from nextTown to P. The
# former will be stored as variables
# in the function, while the latter
# will be computed by recursively
# calling the function: 
# distFromToP(nextTown).

def distFromToP(start):
    # First, we must return the
    # base case, which is when the
    # car is traveling from P to P.
    # In this case, we return 0.
    if (start == "P"):
        return 0
    
    # If the case is not the base
    # case, the program will need to
    # make a choice of which town
    # to get to next using a random
    # number. For readibility, we can
    # generate the random number 
    # here. It will be in [0,1).
    randNum = random()
    
    # Now, we need to go case by
    # case determining which town 
    # to go to and how much the 
    # distance should be.
    if (start == "A"):
        # The comments for this
        # case should be a reference
        # for all other cases, as
        # the program is essentially
        # doing the same thing, except
        # for different towns resulting
        # in different probabilities
        # and distances.

        # According to a certain
        # probability given in the
        # assignment sheet, the car
        # should go to B; otherwise
        # it should go to C. We'll 
        # define this probability here.
        probAtoB = 0.1

        # Since randNum is in [0,1),
        # there is a chance equal to
        # the value of probAtoB that
        # randNum is less than probAtoB.
        # Thus, we should send the car
        # to B if randNum is less than
        # probAtoB.
        if randNum < probAtoB:
            # The distance from A to
            # B is defined here.
            distAtoB = 5

            # To find the distance from
            # A to P, we compute the 
            # sum of the distance from
            # A to B and the distance
            # from B to P.
            return distAtoB + distFromToP("B")
        
        # If the car doesn't travel to
        # B, it instead goes to C.
        else: 
            # Same logic as 
            # previous block

            distAtoC = 6 
            return distAtoC + distFromToP("C")
    if (start == "B"):
        # See case for A for full details
        probBtoD = 0.2
        if randNum < probBtoD:
            distBtoD = 4
            return distBtoD + distFromToP("D")
        # Otherwise goes to E
        else:
            distBtoE = 7
            return distBtoE + distFromToP("E")
    if (start == "C"):
        # See case for A for full details
        probCtoE = 0.3
        if randNum < probCtoE:
            distCtoE = 4
            return distCtoE + distFromToP("E")
        # Otherwise goes to F
        else:
            distCtoF = 6
            return distCtoF + distFromToP("F")    
    if (start == "D"):
        # See A case for details
        probDtoG = 0.1
        if randNum < probDtoG:
            distDtoG = 4
            return distDtoG + distFromToP("G")
        # Otherwise goes to H
        else:
            distDtoH = 6
            return distDtoH + distFromToP("H")
    if (start == "E"):
        # See A case for details
        probEtoH = 0.4
        if randNum < probEtoH:
            distEtoH = 6
            return distEtoH + distFromToP("H")
        # Otherwise goes to I
        else:
            distEtoI = 4
            return distEtoI + distFromToP("I")
    if (start == "F"):
        # See A case for details
        probFtoI = 0.2
        if randNum < probFtoI:
            distFtoI = 3
            return distFtoI + distFromToP("I")
        # Otherwise goes to J
        else:
            distFtoJ = 7
            return distFtoJ + distFromToP("J")
    if (start == "G"):
        # G always goes to K. Thus,
        # return distance from G to K
        # plus distance from K to P.
        distGtoK = 4
        return distGtoK + distFromToP("K")
    if (start == "H"):
        # See A case for details
        probHToK = 0.3
        if randNum < probHToK:
            distHtoK = 4
            return distHtoK + distFromToP("K")
        # Otherwise goes to L
        else:
            distHtoL = 8
            return distHtoL + distFromToP("L")
    if (start == "I"):
        # See A case for details
        probIToL = 0.5
        if randNum < probIToL:
            distItoL = 6
            return distItoL + distFromToP("L")
        # Otherwise goes to M
        else:
            distItoM = 4
            return distItoM + distFromToP("M")
    if (start == "J"):
        # Always goes to M; see
        # case G.
        distJtoM = 5
        return distJtoM + distFromToP("M")
    if (start == "K"):
        # Always goes to N; see
        # case G.
        distKtoN = 4
        return distKtoN + distFromToP("N")
    if (start == "L"):
        # See A case for details
        probLtoN = 0.4
        if randNum < probLtoN:
            distLtoN = 5
            return distLtoN + distFromToP("N")
        # Otherwise goes to O
        else:
            distLtoO = 6
            return distLtoO + distFromToP("O")
    if (start == "M"):
        # Always goes to O; see
        # case G.
        distMtoO = 5
        return distMtoO + distFromToP("O")
    if (start == "N"):
        # Always goes to P; see
        # case G.
        distNtoP = 5
        return distNtoP + distFromToP("P")
    if (start == "O"):
        # Always goes to P; see
        # case G.
        distOtoP = 5
        return distOtoP + distFromToP("P")

# Now that the above function has
# been completed, we can make another
# function called simulate(numCars) 
# which simulates many cars driving
# through the system of towns and 
# computes the average and standard
# deviation of the distances traveled.

def simulate(numCars):
    # First, make a list of travel
    # times by simulating the car
    # numCars times.
    travelTimes = []
    for i in range(numCars):
        # A is defined as the start
        # town in the problem so we
        # always start from A
        travelTimes.append(distFromToP("A"))

    # Now, compute the average 
    # transit time by calculating
    # total transit time (sum of
    # all transit times) and dividing
    # by numCars, and display this
    # value.
    avg = sum(travelTimes)/numCars
    print("The average travel time is: ",avg)

    # Now, compute the variance
    # of the transit times by
    # calculating the sum of the 
    # squares of the differences
    # between the transit times and
    # the average and dividing this
    # result by numCars - 1.
    sumSqrDiff = 0
    for i in range(numCars):
        # Squaring is done by raising
        # to the power of 2
        sumSqrDiff += (travelTimes[i] - avg) ** 2
    var = sumSqrDiff/(numCars - 1)

    # Finally, compute the standard
    # deviation by taking the square
    # root (1/2th power) of variance,
    # and display it.
    stdev = var ** 0.5
    print("The standard deviation of the travel times is: ",stdev)

simulate(100000)