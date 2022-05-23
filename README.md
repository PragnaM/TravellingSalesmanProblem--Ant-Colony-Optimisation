# TravellingSalesmanProblem--Ant-Colony-Optimisation

# Problem:
Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?

# Ant Colony Optimisation:
Ant colony optimization (ACO) is an optimization algorithm, which employs the probabilistic technique and is used for solving computational problems and finding the optimal path with the help of graphs. ACO is inspired by the behavior of ants. At the core of this behavior is the indirect communication between the ants with the help of chemical pheromone trails, which enables them to find short paths between their nest and food sources.
Ants build solutions to TSP by moving on the problem graph from one city to another until they complete a tour. During an iteration of the algorithm each ant builds a tour executing one step for each city. For each ant, transitions from one city to another depend on: Whether or not the city has been visited, the heuristic desirability (“visibility”) of connected cities and the amount of pheromone trail on the edge connecting two cities.

# Working of the Program:
•	User enters the number of cities (N)</br>
•	Symmetric matrix of N x N is created with distances between each city being a random number.</br>
•	Generate a path between the cities</br>
•	For a given number of iterations, repeat:</br>
•	Create a visibility matrix</br>
•	Each ant traverses a random path, visiting every city once</br>
The probability of moving from one city to another is calculated using the formula:</br>
𝑝𝑘 (𝑟, 𝑠) = { 𝜏(𝑟, 𝑠)𝛼 𝜂(𝑟, 𝑠)𝛽 / ∑ 𝜏(𝑟, 𝑢)𝛼 𝜂(𝑟, 𝑢)𝛽         𝑖𝑓 𝑠𝜖𝑀𝑘 </br>
0	𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠e</br>
Where pk(r, s) is probability move from city r to city s of ant k, τ is pheromone level, η(r, s) is visibility of cities r and s, Mk set of cities possibly visited by ant k, α weight of pheromone τ and β is weight to control visibility. </br>
•	Update the pheromone value by taking into consideration the pheromone value added by each ant on the path it traverses and the evaporation rate.</br>
•	We find the optimal solution after a certain number of iterations when all ants converge to the best path which gives minimum distance. </br>
</br>
•	For each iteration, a graph of minimum distance vs iteration is plotted which shows the decrease in the minimum distance as the number of iterations increases, and an optimal solution is obtained.

