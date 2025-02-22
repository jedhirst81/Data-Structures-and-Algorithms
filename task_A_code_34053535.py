
import math, random, time

length = 1000
stall_list = list(range(1, length + 1))

available_stalls = random.sample(stall_list, 500)
stall_position = sorted(available_stalls)

cow_list = random.sample(stall_position, 100)
cow_count = sorted(cow_list)

def aggressive_cows():
    a = (len(stall_position)) / (len(cow_count))
    return(a)


def basic_method():
    
    print("")
    print("Basic method")
    print("")
    
    # print(f"Available stalls: {stall_position}")

    print(f"Cows placed in stalls: {cow_count}")
    print("")
    
    d = aggressive_cows()
    for i in range(len(cow_count) -1):
        if cow_count[i+1] - cow_count[i] < d:
            print(f"Cows too close at stalls {cow_count[i]} and {cow_count [i+1]}")
        else:
            print(f"Distance OK at stalls {cow_count[i]} and {cow_count [i+1]}")

def binary_method():

    print("")
    print("Binary method")
    print("")

    lowerIdx = 0
    upperIdx = (len(stall_list))
    Cow_position = [1, len(stall_list)]
    cows_placed = 2

    while upperIdx - lowerIdx >= 3:
        midPt = (upperIdx + lowerIdx) / 2
        midPt = round(midPt)
        Cow_position.append(midPt)
        Cow_position.sort()
        cows_placed = cows_placed + 1

        print(f"Number of cows = ", (cows_placed))
        print(f"Cows assigned to stalls: {Cow_position}")

        r = random.randint(0, 1)

        if r == 0:
            lowerIdx = midPt
        else:
            upperIdx = midPt
        
        print(f"lowerIdx =",(lowerIdx))
        print(f"upperIdx =",(upperIdx))

binary_method()

def run_comparison():
    
    start = time.thread_time_ns()
    basic_method()
    end = time.thread_time_ns()
    duration_basic = (end - start)/1000000

    
    start = time.thread_time_ns()
    binary_method()
    end = time.thread_time_ns()
    duration_binary = (end - start)/1000000
    
    c = len(cow_list)
    print("")
    print(f"Number of cows:",c)

    print("")
    print("Basic method duration in milliseconds: ",duration_basic)
    print("")
    print("Binary method duration in milliseconds: ",duration_binary)
    print("")

run_comparison()


# References

# SHU Data Structures and Algorithms, Course Materials, 2024

# https://www.geeksforgeeks.org/python-random-sample-function/

# https://www.w3schools.com/python/ref_func_round.asp

# https://www.w3schools.com/python/ref_list_append.asp

