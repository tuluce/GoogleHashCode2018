# Google Hash Code 2018 - Online Qualification Round
#
# A solution which tries to earn the maximum possible bonus points.
# The algorithm draft is given below in pseudocode.
#
# Sort the rides by their starting times.
# Put the rides to a stack with the earliest at the top.
# NextCar := first car of the fleet
# While the stack is not empty,
#   Assign the top ride to the NextCar and pop the ride.
#   Update the NextCar to be the next car in the fleet.
#

def find_starts(rides):
    result = []
    for i in range(len(rides)):
        ride = rides[i]
        result.append((ride[4], ride))
    return result # Consists of tuples (start, [...])

R, C, F, N, B, T = [int(i) for i in input().split()]
rides = []
starts = []
for i in range(N):
    rides.append([int(i) for i in input().split()] + [i])

starts = find_starts(rides)
starts.sort(reverse=True)

cars = []
for c in range(F):
    cars.append([])

c = 0
while starts:
    st = starts.pop()
    cars[c].append(st[1][-1])
    c = (c+1) % F
    
for car in cars:
    if (len(car)):
        print(len(car), end=" ")
        print(" ".join(str(c) for c in car))
    else:
        print(0)
