
import numpy as np
from random import uniform
from matplotlib import pyplot as plt

def get_nodes(number_of_cities):
    distancematrixhalf = np.random.randint(0,100,size=(number_of_cities,number_of_cities)) # random symmetric matrix
    distancematrix = (distancematrixhalf + distancematrixhalf.T)
    for i in range (0,number_of_cities):
        distancematrix[i][i]=0 # diagonal elements=0
    print (distancematrix)
    return distancematrix

NUMBER_OF_ITERATIONS = 300  
EVAPORATION_FACTOR = 0.5 
UPDATED_PHEROMONE_VALUE = 7  
ALPHA = 1  
BETA = 1  


def iterate_ants(ants, edges, number_of_cities):
    trails1 = []
    for a in ants:
      
        visited = [0] * number_of_cities
        trail = []
        count = 0
        q = a
        visited[q] = 1
        trail.append(q)
        while count < number_of_cities - 1:
            
            sum1 = 0
            numerator = []
            prob = []
            sub_visit = [0] * number_of_cities
            for v in range(len(visited)):
                if visited[v] == 1:
                    sub_visit[v] = 1
            for p in range(number_of_cities):
                if sub_visit[p] == 0:
                    this_edge = edges[(number_of_cities * p) + q]
                    ph = this_edge[2]
                    w = this_edge[1]
                    ph = ph ** ALPHA
                    w = w ** BETA
                    if w == 0:
                        num = float('inf')
                    else:
                        num = ph / w
                    numerator.append((p, num))
                    sum1 += num
            for v in range(len(numerator)):
                prob.append((numerator[v][0], numerator[v][1] / sum1))
            seed = uniform(0, 1)
            sum2 = 0
            temp = None
            for p in range(len(prob)):
                sum2 += prob[p][1]
                if sum2 < seed:
                    continue
                else:
                    temp = prob[p][0]
                    break
            visited[temp] = 1
            trail.append(temp)
            count += 1
            q = temp
        trails1.append(trail)
    return trails1


def update_edge(a, b, edges, number_of_cities):
    this1 = edges[(number_of_cities * a) + b]
    this2 = edges[(number_of_cities * b) + a]
    w1 = this1[1]
    w2 = this2[1]
    ph1 = this1[2]
    ph2 = this2[2]
  
    edges[(number_of_cities * a) + b] = ((a, b), w1, ph1 + UPDATED_PHEROMONE_VALUE)
    edges[(number_of_cities * b) + a] = ((b, a), w2, ph2 + UPDATED_PHEROMONE_VALUE)


def update_pheromone_and_find_best_path(ts, distancematrix, edges, number_of_cities):
    min1 = float('inf')
    min_path1 = []
    for t in ts:
        sum1 = 0
        for i in range(len(t) - 1):
            a = t[i]
            b = t[i + 1]
            sum1 += distancematrix[a][b]
            update_edge(a, b, edges, number_of_cities)
        if min1 > sum1:
            min1 = sum1
            min_path1 = []
            min_path1 += t
    ret_path = min_path1[:]
    ret_path.append(min_path1[0])
    min1 += distancematrix[min_path1[-1]][ min_path1[0]]
    return min1, ret_path


def evaporation(edges, number_of_cities):
    for e in edges:
        p1 = e[0][0]
        p2 = e[0][1]
        w = e[1]
        ph = e[2]
        edges[(number_of_cities * p1) + p2] = ((p1, p2), w, ph * EVAPORATION_FACTOR)


def execute(distancematrix, number_of_cities):
    counter2 = 0
    print()
    print("Ant Colony Optimization")
    
    edges = []
    for x in range(number_of_cities):
        for y in range(number_of_cities):
            if x is not y:
                edges.append(((x, y), distancematrix[x][y], 1))
            else:
                edges.append(((x, y), float("inf"), 1))
    global_minima = float('inf')
    global_min_path = []
    plot_x = []
    plot_y = []

    for r in range(NUMBER_OF_ITERATIONS):
        ants = list(range(number_of_cities))
        print(len(ants))
        trails = iterate_ants(ants, edges, number_of_cities)
        min_value, min_path = update_pheromone_and_find_best_path(trails, distancematrix, edges, number_of_cities)
        evaporation(edges, number_of_cities)
        if global_minima > min_value:
            global_minima = min_value
            global_min_path = min_path
        counter2 += 1
        print(counter2, ': ', min_value, '     ', min_path)
        plot_x.append(counter2)
        plot_y.append(min_value)

    print()
    print('Best path from ant colony optimisation : ', global_min_path, '     ', global_minima)



    plt.plot(plot_x, plot_y)
    plt.xlabel("Iteration")
    plt.ylabel("Minimum Distance")
    
    plt.show()


number_of_cities = input('Enter number of cities: ')
NUMBER_OF_CITIES = int(number_of_cities)
if NUMBER_OF_CITIES < 2:
    NUMBER_OF_CITIES = 2
distance_matrix = get_nodes(NUMBER_OF_CITIES)

execute(distance_matrix, NUMBER_OF_CITIES)


