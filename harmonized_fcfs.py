#!/usr/bin/python3

"""

This Python script contains research paper's queue-finding algorithm and emulates the proposed harmonized FCFS algorithm using data displayed in the paper.

Research paper mentioned: https://ieeexplore.ieee.org/abstract/document/10379263

"""

def FindQueue(A: list):
    """
    Determines which queue, given a list of the queues' size, is less
    then returns the position of that queue.
    """
    for i in range(len(A)):
        if A[i] == 0:
            position = i
            A[i] = A[i] + 1
            return position

        for i in range(len(A) - 1):
            min = i
            for j in range(i + 1, len(A)):
                if A[j] < A[min]:
                    min = j

            position = min
            A[min] = A[min] + 1
            return position

cars = [
    # Cars, Arrival, Burst
    ("C1", 0, 2),
    ("C2", 0, 10),
    ("C3", 2, 10),
    ("C4", 3, 2),
    ("C5", 4, 2),
    ("C6", 6, 2),
    ("C7", 9, 5),
    ("C8", 12, 2),
    ("C9", 15, 2),
    ("C10", 15, 10)
]

cars.sort(key=lambda c: c[1])

num_queues = 2
queue = [0] * num_queues
assigned_queues = [[] * num_queues]

for i in range(len(cars)):
    car, arrival, burst = cars[i]

    if burst < 10:
        assigned_queues[0].append(cars[i])
    else:
        assigned_queues[1].append(cars[i])


ET = [] # finish_time - burst
TAT = [] # finish_time - arrival
WT = [] # finish_time - arrival - burst

for c in assigned_queues[0]:
    print(c)

print("====================")

for c in assigned_queues[1]:
    print(c)
