#!/usr/bin/python3

"""

This Python script contains and shows an improvement to the proposed algorithm from the research paper by dynamically reallocating overloaded queues.

Research paper mentioned: https://ieeexplore.ieee.org/abstract/document/10379263

"""

############## Global Variables ##############

# The processes
cars = [
    # Name, Arrival, Burst
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

# Sorts the list of processes by their arrival time
cars.sort(key=lambda c: c[1])

# Set up the queues
MAX_QUEUE_LEN = 4   # Max number of processes in each queue
num_queues = 2      # Number of queues to start with

# Initialize the queues
assigned_queues = [[] for _ in range(num_queues)]

################ Functions ###################

# Custom types for type hinting in functions
type Process = tuple[str, int, int]
type Scheduled_Process = tuple[str, int, int, int]

type Queue = list[Process]
type Scheduled_Queue = list[Scheduled_Process]
type Queue_Group = list[Queue | Scheduled_Queue]

def FindQueue(A: list[int]) -> int:
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

    raise Exception("FindQueue unable to find a queue!")


def init(processes: Queue):
    low_queue = []
    high_queue = []
    
    for p in processes:
        _, _, burst = p

        if burst < 10:
            low_queue.append(p)
        else:
            high_queue.append(p)

    assigned_queues[0].append(low_queue)
    assigned_queues[1].append(high_queue)


def split_overloaded_queues(queues: list[Queue_Group]):
    for i in range(len(queues)):
        queue_group = queues[i]

        for j in range(len(queue_group)):
            queue = queue_group[j]

            if len(queue) > MAX_QUEUE_LEN:
                A_tmp = [0, 0]
                queue_tmp = [[], []]

                for p in queue:
                    pos = FindQueue(A_tmp)
                    queue_tmp[pos].append(p)

                queue_group[j] = queue_tmp[0]
                queue_group.append(queue_tmp[1])


def FCFS(processes: Queue) -> Scheduled_Queue:
    new_processes = []
    time = 0

    for p in processes:
        process, arrival, burst = p

        if time < arrival:
            time = arrival

        exit_time = time + burst
        turn_around = exit_time - arrival
        wait_time = turn_around - burst

        time = exit_time

        new_processes.append((process, arrival, burst, wait_time))

    return new_processes


def print_queues(queues: list[Queue_Group]):
    queue_group_idx = 1
    
    for queue_group in queues:
        print(f"Queue Group: {queue_group_idx}:")
        queue_idx = 1

        for queue in queue_group:
            print(f"Queue: {queue_group_idx}-{queue_idx}:")
            for p in queue:
                print("\t" + str(p))

            queue_idx += 1
            print("-" * 10)

        queue_group_idx += 1
        print("=" * 20, end="\n\n")

##############################################

###### Main execution ######

# Initial classification
init(cars)

# Find overloaded queues and split them up
split_overloaded_queues(assigned_queues)

# Run FCFS on all queues
for i in range(len(assigned_queues)):
    queue_group = assigned_queues[i]

    for j in range(len(queue_group)):
        queue_group[j] = FCFS(queue_group[j][:])

print_queues(assigned_queues)
