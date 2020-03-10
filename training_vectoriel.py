import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def normalizeFonction(datas):
    return datas / (max(datas))

def Gradient_descent(thetas, X, y):
    learning_rate = 1.5
    while (1):
        tmp = thetas
        thetas = thetas - learning_rate * ((1 / len(X)) * (X.T @ ((X @ thetas) - y)))
        if np.array_equal(thetas, tmp):
            break
    return thetas
      
if __name__ == "__main__":
    dataset = pd.read_csv('data.csv')
    X = np.array(dataset.iloc[:, :-1].values)
    X_plot = X
    X = normalizeFonction(X)
    X = np.c_[np.ones(X.shape[0]), X]
    y = np.array(dataset.iloc[:, -1].values)
    y_plot = y
    y = normalizeFonction(y)
    thetas = np.array([0,0])
    thetas = Gradient_descent(thetas, X, y)
    thetas[0] = thetas[0] * max(y_plot)
    thetas[1] = thetas[1] * (max(y_plot) / max(X_plot))
    X_func = np.c_[np.ones(X_plot.shape[0]), X_plot]
    df = pd.DataFrame({"theta0": [thetas[0]], "theta1": [thetas[1]]})
    df.to_csv('theta.csv')
    plt.scatter(X_plot, y_plot, color = 'blue')
    plt.plot(X_plot, X_func @ thetas, color = 'green')
    plt.title('Prix voiture')
    plt.xlabel('kilometre')
    plt.ylabel('Prix')
    plt.show()
