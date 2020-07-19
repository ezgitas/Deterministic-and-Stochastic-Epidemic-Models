import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def contactnetwork(population):
	pop_network = np.zeros((population,population))
	for i in range(population):
		for j in range(days):
			pop_network[i][j] = np.random.randint(2)
			pop_network[j][i] = pop_network[i][j]
	return pop_network
	
def contamination(days,population,pop_matrix):
	for i in range(1,days+1):
		for j in range(population):


population = 11
days = 10
pop_matrix = np.zeros((days,population))
x = np.random.randint(population)
pop_matrix[0][x] = 1

G = nx.Graph(contactnetwork(population))
plt.subplot(121)
nx.draw(G,with_labels=True, font_weight='bold')
plt.show()

#print(G)