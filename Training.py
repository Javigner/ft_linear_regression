# Importer les librairies
import matplotlib.pyplot as plt
import pandas as pd

def prediction(theta0, theta1, test_value):
    return (theta0 + theta1 * test_value)

def cost_function_theta0(theta0, theta1, X, y):
    result = 0
    for i in range(len(X)):
        result = float(result + (theta0 + theta1 * X[i] - y[i]))
    costf = (1 / (2 * len(X))) * result
    return costf

def cost_function_theta1(theta0, theta1, X, y):
    result = 0
    for i in range(len(X)):
        result = float(result + (theta0 + theta1 * X[i] - y[i]) * X[i])
    costf = (1 / (2 * len(X))) * result
    return costf

def Gradient_descent(theta0, theta1, X, y):
    learning_rate = 0.001
    tmptheta0 = float(0)
    tmptheta1 = float(0)
    while (theta0 != tmptheta0 and theta1 != tmptheta1):
        theta0 = tmptheta0
        theta1 = tmptheta1
        tmptheta0 = theta0 - learning_rate * (1 / len(X)) * cost_function_theta0(theta0, theta1, X, y)
        tmptheta1 = theta1 - learning_rate * (1 / len(X)) * cost_function_theta1(theta0, theta1, X, y) 
    return (theta0, theta1)
    
def main():
    dataset = pd.read_csv('Data.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    theta0 = float(0)
    theta1 = float(0)
    theta0, theta1 = Gradient_descent(theta0, theta1, X, y)
    print(prediction(theta0, theta1, 240000))
    
if __name__ == "__main__":
	main();
