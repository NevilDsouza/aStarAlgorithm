from helper import *

startCity = Node(0)
destinationCity = Node(19)

closedCities = []

pQueue = PriorityQueue()

pQueue.push(startCity)

head = pQueue.front


while head != None and head.nodeName != destinationCity.nodeName:
    citiesToPush = []
    for city, pathCost in cityDistances[head.nodeName].items():
        pathCost = cityDistances[head.nodeName][city] + head.pathCost
        cityLoc = pQueue.search(city)

        if not cityLoc and city != head.nodeName:
            citiesToPush.append(
                Node(city, pathCost, pathCost + heurDist[city], head.nodeName))
        elif cityLoc.pathCost > pathCost:
            cityLoc.pathCost = pathCost
            cityLoc.combinedCost = pathCost + heurDist[city]
            cityLoc.parentNode = head.nodeName

    closedCities.append(pQueue.pop())

    for city in citiesToPush:
        pQueue.push(city)

    head = pQueue.front

route = []
while head != startCity:
    route.append(head)

    for nextCity in closedCities:
        if head.parentNode == nextCity.nodeName:
            head = nextCity
            break

routeCost = head.combinedCost

route.append(head)
route.reverse()


space = "-"*10
print(space + "Route" + space)
for city in route:
    print(city)

print(f'\nDistance from {cities[19]} to {cities[1]}: {route[-1].combinedCost}')
