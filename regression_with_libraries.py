import matplotlib.pyplot as plt
import pandas as pd

# Importer le dataset
dataset = pd.read_csv('data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Construction du modèle
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)

# Faire de nouvelles prédictions
print(regressor.predict([[69000]]))

# Visualiser les résultats
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Prix  de la voiture')
plt.xlabel('Kilomètre')
plt.ylabel('Prix')
plt.show()