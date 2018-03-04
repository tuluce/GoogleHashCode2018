# Google Hash Code 2018 - Online Qualification Round
#
# A solution which does not considers the start and finish times.
# The algorithm draft is given below in pseudocode.
#
# For each car,
#   TimeLeft := SimulationTime
#   While TimeLeft > 0 for this car,
#     Choose the ride with closest starting point to the current location.
#     Decrement the TimeLeft according to this ride.
#     Update the current location.
#     Assign this ride to the current car.
#

def distance(start, stop):
    return abs(start[0] - stop[0]) + abs(start[1] - stop[1])

def find_distances(start, stops):
    result = []
    for stop in stops:
        result.append((distance(start, stop), stop))
    return result # Consists of tuples (distance, [...])

R, C, F, N, B, T = [int(i) for i in input().split()]
rides = []
starts = []
for i in range(N):
    rides.append([int(i) for i in input().split()] + [i])

cars = []
for c in range(F):
    car = []
    timeLeft = T
    carPos = [0, 0]
    while timeLeft > 0:
        distances = find_distances(carPos, rides)
        if not distances: break
        nextPos = min(distances)
        if timeLeft - nextPos[0] - distance([nextPos[1][0], nextPos[1][1]], [nextPos[1][2], nextPos[1][3]]) >= 0:
            timeLeft -= nextPos[0] + distance([nextPos[1][0], nextPos[1][1]], [nextPos[1][2], nextPos[1][3]])
            rides.remove(nextPos[1])
            car.append(nextPos[1][-1])
            carPos = [nextPos[1][2], nextPos[1][3]]
        else:
            break
    cars.append(car)
    
for car in cars:
    if (len(car)):
        print(len(car), end=" ")
        print(" ".join(str(c) for c in car))
    else:
        print(0)
