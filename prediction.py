import pandas as pd
import matplotlib.pyplot as plt

def prediction(theta0, theta1, X):
    return theta0 + theta1 * X

def prediction_plot(theta0, theta1, X):
    liste = []
    for i in range(len(X)):
        liste.append(float(theta0 + theta1 * X[i]))
    return (liste)

def main():
    data = pd.read_csv('theta.csv')
    theta0 = data.at[0, 'theta0']
    theta1 = data.at[0, 'theta1']
    dataset = pd.read_csv('data.csv')
    X_train = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    X = 0
    while (X <= 0):
        X = input("Saisissez un Kilomètrage pour estimer le prix de votre voiture : ")
        try:
            X = int(X);
        except:
            print("Vous n'avez pas saisi un kilomètrage valide. Merci de réessayer.");
            X = 0;
            if (X < 0):
                print("Kilomètrage inferieur à 0. Merci de réessayer.");
    pred = prediction(theta0, theta1, X)
    print("L'estimation de votre voiture est de " + str(int(pred)) + "`");
    if (pred != 0 and theta0 != 0 and theta1 != 0):
        plt.scatter(X_train, y, color = 'red', s = 20, marker = '*')
        plt.scatter(X, pred, color = 'green', s = 150, marker = 'o')
        plt.plot(X_train, prediction_plot(theta0, theta1, X_train), color = 'blue')
        plt.title('Prix voiture')
        plt.xlabel('kilometre')
        plt.ylabel('Prix')
        plt.show()
    

if __name__ == "__main__":
	main();
