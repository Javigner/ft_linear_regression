import pandas as pd

def prediction(theta0, theta1, X):
    return theta0 + theta1 * X

def main():
    data = pd.read_csv('theta.csv')
    theta0 = data.at[0, 'theta0']
    theta1 = data.at[0, 'theta1']
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
    print("L'estimation de votre voiture est de " + str(int(pred)) + "$");
    

if __name__ == "__main__":
	main();
