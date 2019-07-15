import pandas as pd
import matplotlib.pyplot as plt

def prediction(theta0, theta1, test_value):
    return float(theta0 + theta1 * test_value)

def prediction_plot(theta0, theta1, X):
    liste = []
    for i in range(len(X)):
        liste.append(float(theta0 + theta1 * X[i]))
    return (liste)

def cost_function_theta0(theta0, theta1, X, y):
    result = 0
    for i in range(len(X)):
        result += ((theta0 + theta1 * X[i]) - y[i])
    return result

def cost_function_theta1(theta0, theta1, X, y):
    result = 0
    for i in range(len(X)):
        result += ((theta0 + theta1 * X[i]) - y[i]) * X[i]
    return result

def mean_normalization(liste):
	liste2 = []
	for x in range(len(liste)):
		liste2.append(liste[x] / max(liste))
	return(liste2);
    
def Gradient_descent(theta0, theta1, X, y):
    learning_rate = 1
    tmp0 = float(2)
    tmp1 = float(2)
    X = mean_normalization(X)
    y = mean_normalization(y)
    while (theta0 != tmp0 and theta1 != tmp1):
        tmp0 = theta0
        tmp1 = theta1
        tmptheta0 = theta0 - learning_rate * (1.0 / len(X)) * cost_function_theta0(theta0, theta1, X, y)
        tmptheta1 = theta1 - learning_rate * (1.0 / len(X)) * cost_function_theta1(theta0, theta1, X, y)
        theta0 = tmptheta0
        theta1 = tmptheta1
        
        
    return (theta0, theta1)
    
def main():
    dataset = pd.read_csv('Data.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    theta0 = float(0)
    theta1 = float(0)
    theta0, theta1 = Gradient_descent(theta0, theta1, X, y)
    theta0 = theta0 * max(y)
    theta1 = theta1 * (max(y) / max(X))
    df = pd.read_csv('theta.csv')
    df.at[0, 'theta0'] = theta0
    df.at[0, 'theta1'] = theta1
    df.to_csv('theta.csv', index=False)
    plt.scatter(X, y, color = 'red')
    plt.plot(X, prediction_plot(theta0, theta1, X), color = 'blue')
    plt.title('Prix voiture')
    plt.xlabel('kilometre')
    plt.ylabel('Prix')
    plt.show()
      
if __name__ == "__main__":
	main();
