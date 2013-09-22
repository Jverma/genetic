#genetic algorithm in python
#Janu Verma
#http://randominferences.tumblr.com/
###############################################################################

import math
import random




#define the fitness function, here it is a straight line.   
def fitness_function(x, y, parameters):
    a = parameters[0]
    b = parameters[1]
    chi2 = 0.0
    for i in range(len(x)):
        y_new = a*x[i] + b
        chi2 = chi2 + ((y_new - y[i]/(y[i]*0.5)))**2
    return chi2/len(x)


#####################################################################################################
#DON'T CHANGE BELOW THIS
#####################################################################################################

#selection of parents
def selection(f,pop_size):		
	f_inv = []				    #making a list for inverse of fitness	
	for i in range(pop_size):		    #doing inverse of individual fitness
	    f_inv.append(1./f[i])	
        sumf_inv = sum(f_inv)	
	randomsum = random.random()*sumf_inv	    #Generating random number betwee 0 and sum of inverse fitness
	f_compare = 0.				
	for i in range(pop_size):		    #Comparing summing over individual fitnesses
		f_compare = f_compare + f_inv[i]
		if f_compare > randomsum:
			break			    #when summing is greater than random number, that index is returned and chain is broken
	return i


#n be number of chromosomes 
# vec is a list of initial solutions
#mutation
def mutation(vec, step, mut_prob):
    i = random.randint(0, len(vec) - 1)
    size = step + mut_prob*random.gauss(0.0, 1.0)
    return vec[0:i]+[vec[i]+size]+vec[i+1:]         #change the ith element of the vector by the user specified step.



#crossover
def crossover(vec1, vec2, cross_prob):
    i=int(cross_prob*len(vec1))
    return vec1[0:i]+vec2[i:]




#max is maximum value of the parameters
#min is the minimum value of the parameters
# I've taken the max and min same for all the parameters
#this can be changed by supplying a list of length n containing 2-tuples
#i.e. min and max for each parameter
#pop_size is the size of the population
#n is mumber of parameters
#initial solution
def chromosomes(pop_size, min, max, n):
    pop=[]
    for i in range(pop_size):
        vec=[random.randint(min,max) for i in range(n)]
        pop.append(vec)
    return pop




#genetic algorithm
def genetic_alg(f, x_data, y_data, population, threshold, fitness_limit, cross_prob, mut_prob, mut_step):
    pop = []
    fitness = []
    while (threshold > fitness_limit):
        for i in range(len(population)):
            f_values = [f[j] for j in range(len(population))]
            #sorted_values = sorted(fun_values, reverse=True)
            index1 = selection(f_values, len(population))
            index2 = selection(f_values, len(population))
            elite1 = population[index1]
            elite2 = population[index2]
            new_gen = crossover(elite1, elite2, cross_prob)
            new_gen = mutation(new_gen, mut_step, mut_prob)        
            pop.append(new_gen)
            fitness.append(fitness_function(x_data, y_data, new_gen))    
        mean_fitness = sum(fitness)/len(fitness)
        min_fitness = mean_fitness
        if (min_fitness < threshold):
            threshold = min_fitness
        else:
            threshold = threshold
    best_fitness = threshold        
    for j in range(len(fitness)):
        if (fitness[j] == best_fitness):
            parameters_estimated = pop[j]
            break 
    return best_fitness, parameters_estimated       
    
                    



