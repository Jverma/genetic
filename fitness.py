import math
import random
import sys
import genetic


#Enter the data, here it is x and corresponding y values.
x_data = []
y_data = []
input_data = open(sys.argv[1])          #input is a tab separated file containing data
for line in input_data:
    data = line.split('\t')
    x_data.append(int(data[0]))
    y_data.append(int(data[1]))




pop_size = 100
min = 1.0
max = 10.0
n = 2                           #number of parameters
population = genetic.chromosomes(pop_size, min, max, n)

cross_prob = 0.5
mut_prob = 0.2
mut_step = 1.0
threshold = 0.5
fitness_limit = 0.005
f = [genetic.fitness_function(x_data, y_data, p) for p in population]
results_genetic = genetic.genetic_alg(f, x_data, y_data, population, threshold, fitness_limit, cross_prob, mut_prob, mut_step)
print results_genetic
