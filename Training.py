# Importer les librairies
import matplotlib.pyplot as plt
import pandas as pd
from math import pow

# Importer le dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
theta0 = float(0)
theta1 = float(0)
x_test = 240000
lentest = len(X)

def prediction(theta0, theta1, test_value):
    return (theta0 + theta1 * test_value)

def cost_function(theta0, theta1, X, y):
    result = 0
    for i in range(len(X)):
        result = float(result + pow((theta0 + theta1 * X[i] - y[i]), 2))
    costf = (1 / (2 * len(X))) * result
    return costf

def Gradient_descent(theta0, theta1, X, y):
    learning_rate = 0.001
    tmptheta0 = float(0)
    tmptheta1 = float(0)
    while (theta0 != tmptheta0 & theta1 != tmptheta1):
        theta0 = tmptheta0
        theta1 = tmptheta1
        tmptheta0 = theta0 - learning_rate * [] * cost_function(theta0, theta1, X, y)
        tmptheta1 = theta1 - learning_rate * [] * cost_function(theta0, theta1, X, y)
    return (theta0, theta1)
    
def linear_regression(X, y, theta0, theta1, x_test):
    pred = theta0 + theta1 * x_test
    somme = sum(X)
    
 print(cost_function(theta0, theta1, X, y))   

