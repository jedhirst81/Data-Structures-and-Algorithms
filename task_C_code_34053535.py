
import random
import time

random_list = random.sample(range(1, 50000), 10000)
  
# bubble sort function
def bubble_sort(random_list):
    iteration_number = len(random_list)-1
    for i in range(iteration_number,0,-1):
        for j in range(i):
            if random_list[j] > random_list[j+1]:
                temp = random_list[j]
                random_list[j] = random_list[j+1]
                random_list[j+1] = temp
    sorted_list = random_list

# binary heap function
def tidy_heap(heap, index):
    LEFT = (2 * index) + 1
    RIGHT = (2 * index) + 2

    large = index
    if LEFT < len(heap) and heap[large] < heap[LEFT]:
        large = LEFT
    if RIGHT < len(heap) and heap[large] < heap[RIGHT]:
        large = RIGHT
        
    if large != index:
        heap[index], heap[large] = heap[large], heap[index]
        tidy_heap(heap, large)
    return heap

def heap_sort(random_list):
    sort_array = []
    heap = random_list.copy()
    while heap:
        sort_array.insert(0, heap[0])
        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop(-1)
    
    return sort_array
    
# experiment function which calls bubble sort function and binary heap function(class) and records their times
def run_experiment():
    l = len(random_list)
    print("Array size",(l))
    start = time.thread_time_ns()
    bubble_sort(random_list)
    end = time.thread_time_ns()
    duration_nano = (end - start)/1000000
    print("Bubble sort duration in milliseconds: ",duration_nano)
    start = time.thread_time_ns()
    heap_sort(random_list)
    end = time.thread_time_ns()
    duration_nano = (end - start)/1000000
    print("Heap sort duration in milliseconds: ",duration_nano)

# call experiment function, passing in values of randomly generated list
run_experiment()


# References
# https://www.geeksforgeeks.org/generating-random-number-list-in-python/

# https://www.geeksforgeeks.org/binary-heap-in-python/

# Heaps and Heap Sort in Python (Tutorial):
# https://www.youtube.com/watch?v=V1K7bYcAhXY
