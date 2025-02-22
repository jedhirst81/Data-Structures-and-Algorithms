
import random
import copy

class scales_problem:

    def __init__(self, data):
        self.data = data
        self.solution = [random.randint(0,1) for i in range(len(data))]
        self.fitness = 0.00
        self.calculate_fitness()

    def print_solution(self):
        for i in self.solution:
            print (i, end=" ")
        print("\t")

    def calculate_fitness(self):
        left_weight = 0
        right_weight = 0
        for i in range(len(self.data)):
            if self.solution[i] == 0:
                left_weight += (self.data[i])
            else:
                right_weight += (self.data[i])

        self.fitness = abs(left_weight-right_weight)

    def copy_solution(self, another_scales):
        self.solution = copy.deepcopy(another_scales.solution)
        self.calculate_fitness()

data = random.sample(range(1, 100), 20)

print(data)

scale = scales_problem(data)
scale.print_solution()
scale.calculate_fitness()
fitness = scale.fitness
print("Fitness is:", (fitness))


class Hill_Climbing:

    def __init__(self, data):
        self.solution1 = scales_problem(data)
        self.solution2 = scales_problem(data)
        self.solution2.copy_solution(self.solution1)

    def small_change(self):
        for i in range(2):
            j = random.randint(0,len(self.solution2.solution)-1)
            if self.solution2.solution[j] == 0:
                self.solution2.solution[j] = 1
            else:
                self.solution2.solution[j] = 0
        self.solution2.calculate_fitness()

    def small_change2(self):
        random_index = []

        for i in range(2):
            index = random.randint(0, len(self.solution2.solution)-1)

            while(index in random_index):
                index = random.randint(0, len(self.solution2.solution) - 1)

            if self.solution2.solution[index] == 0:
                self.solution2.solution[index] = 1
            else:
                self.solution2.solution[index] = 0

            random_index.append(index)
        self.solution2.calculate_fitness()

    def run_hc(self, it):

        results = []
        print("Initial solution : ")
        self.solution1.print_solution()

        counter = 1
        for i in range(it):

            row = []
            print("Iter ",i)
            self.small_change2()
            print("New solution: ")
            self.solution2.print_solution()
            print(self.solution2.fitness)

            print("Current solution: ")
            self.solution1.print_solution()
            print(self.solution1.fitness)

            if self.solution2.fitness < self.solution1.fitness:
                self.solution1.copy_solution(self.solution2)

            row.append(counter)
            row.append(self.solution1.fitness)
            row.append(self.solution1.solution)
            results.append(row)
            counter+=1
            print()

    def print_results(self, results):
        counter = 0
        for row in results:
            print(counter)
            print(row)
            counter+=1


climb = Hill_Climbing(data)

climb.run_hc(10)  


# References

# SHU Data Structues and Algorithms module course materials, 2024.

# Agarwal, B. (2022). Hands-on data structures and algorithms with Python: store, manipulate, and access data effectively and boost the performance of your applications. Packt Publishing.

# Edelkamp, S. & Schroedl, S. (2011). Heuristic Search: Theory and Applications. Morgan Kaufmann.
