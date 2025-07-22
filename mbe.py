import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def estimate_reserves_mbe(csv_path):
    df = pd.read_csv(csv_path)
    X = df['Eo'].values.reshape(-1, 1)
    y = df['F'].values
    model = LinearRegression().fit(X, y)
    N = model.coef_[0]
    return N, model

def plot_mbe(csv_path, model):
    df = pd.read_csv(csv_path)
    X = df['Eo'].values.reshape(-1, 1)
    y = df['F'].values
    y_pred = model.predict(X)

    plt.scatter(X, y, label='Actual')
    plt.plot(X, y_pred, color='red', label='Regression Line')
    plt.xlabel("Eo")
    plt.ylabel("F")
    plt.title("Material Balance: F vs Eo")
    plt.legend()
    plt.grid(True)
    plt.show()
