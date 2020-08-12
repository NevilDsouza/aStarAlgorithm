
class Node:
    def __init__(self, nodeName=None, pathCost=0, combinedCost=0, parentNode=None):
        self.nodeName = nodeName
        self.pathCost = pathCost
        self.combinedCost = combinedCost
        self.parentNode = parentNode
        self.next = None

    def __str__(self):
        string = "-"*25
        string += f'\nnodeName: {self.nodeName}\npathCost: {self.pathCost}\ncombinedCost: {self.combinedCost}\nparentNode : {self.parentNode}\n'
        string += "-"*25

        return string


class PriorityQueue:
    def __init__(self):
        self.front = None

    def push(self, node):
        if (self.front == None):
            self.front = self.rear = node
        elif(self.front.combinedCost > node.combinedCost):
            node.next = self.front
            self.front = node
        else:
            head = self.front

            while head.next != None and head.next.combinedCost <= node.combinedCost:
                head = head.next

            node.next = head.next
            head.next = node

    def pop(self):
        if self.front == None:
            print("Queue Underflow")
            deletedNode = None
        else:
            deletedNode = self.front
            self.front = self.front.next

        return deletedNode

    def print(self):
        head = self.front

        while head != None:
            print(head)
            head = head.next

    def isEmpty(self):
        return self.front == None

    def search(self, cityName):
        head = self.front

        while head != None:
            if head.nodeName == cityName:
                return head
            head = head.next

        return False


heurDist = {
    0: 366,
    1: 0,
    2: 160,
    3: 242,
    4: 161,
    5: 176,
    6: 77,
    7: 151,
    8: 226,
    9: 244,
    10: 241,
    11: 234,
    12: 380,
    13: 98,
    14: 193,
    15: 253,
    16: 329,
    17: 80,
    18: 199,
    19: 374
}

cities = {
    0: "Arad",
    1: "Bucharest",
    2: "Craiova",
    3: "Dobreta",
    4: "Eforite",
    5: "Fagaras",
    6: "Giurgiu",
    7: "Hirsova",
    8: "lasi",
    9: "Lugoj",
    10: "Mehadia",
    11: "Neamt",
    12: "Oradea",
    13: "Pitesti",
    14: "Rimnicu Vilcea",
    15: "Sibiu",
    16: "Timisora",
    17: "Urziceni",
    18: "Vaslui",
    19: "Zerind"
}

cityDistances = [
    {15: 140, 16: 118, 19: 75},
    {5: 211, 6: 90, 13: 101, 17: 85},
    {3: 120, 13: 138, 14: 146},
    {2: 120, 10: 75},
    {7: 86},
    {1: 211, 15: 99},
    {1: 90},
    {4: 86, 17: 98},
    {11: 87, 18: 92},
    {10: 70, 16: 111},
    {3: 75, 9: 70},
    {8: 87},
    {15: 151, 19: 71},
    {1: 101, 2: 138, 14: 97},
    {2: 146, 13: 97, 15: 80},
    {0: 140, 5: 99, 12: 151, 14: 80},
    {0: 118, 9: 111},
    {1: 85, 7: 98, 18: 142},
    {8: 92, 17: 142},
    {0: 75, 12: 71}
]
