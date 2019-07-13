# Import the libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the data and create matrices
my_data = np.genfromtxt('data.csv', delimiter=',') # read the data
X = my_data[1:, 0].reshape(-1,1) # -1 tells numpy to figure out the dimension by itself
ones = np.ones([X.shape[0], 1]) # create a array containing only ones 
X = np.concatenate([ones, X],1) # cocatenate the ones to X matrix
y = my_data[1:, 1].reshape(-1,1) # create the y matrix

# Visualize data
plt.scatter(my_data[1:, 0], y)

# Set the hyper parameters

# notice small alpha value
alpha = 0.0001
iters = 10

# theta is a row vector
theta = np.array([[1.0, 1.0]])

# Create the cost function
def computeCost(X, y, theta):
    inner = np.power(((X @ theta.T) - y), 2) # @ means matrix multiplication of arrays. If we want to use * for multiplication we will have to convert all arrays to matrices
    return np.sum(inner) / (2 * len(X))

computeCost(X, y, theta)

# Create the Gradient Descent function
def gradientDescent(X, y, theta, alpha, iters):
    for i in range(iters):
        theta = theta - (alpha/len(X)) * np.sum((X @ theta.T - y) * X, axis=0)
        cost = computeCost(X, y, theta)
        # if i % 10 == 0: # just look at cost every ten loops for debugging
        #     print(cost)
    return (theta, cost)

g, cost = gradientDescent(X, y, theta, alpha, iters)  
print(g, cost)