# dca.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def perform_dca(filepath='data/dca_production_data.csv'):
    # Load the production data CSV
    data = pd.read_csv(filepath)
    t = data['time_days'].values
    q = data['production_rate'].values

    # Decline models
    def exponential(t, qi, D):
        return qi * np.exp(-D * t)

    def harmonic(t, qi, D):
        return qi / (1 + D * t)

    def hyperbolic(t, qi, D, b):
        return qi / (1 + b * D * t)**(1/b)

    # Curve fitting
    popt_exp, _ = curve_fit(exponential, t, q, maxfev=10000)
    popt_har, _ = curve_fit(harmonic, t, q, maxfev=10000)
    popt_hyp, _ = curve_fit(hyperbolic, t, q, bounds=([0, 0, 0], [np.inf, 1, 1]), maxfev=10000)

    # Prediction
    t_pred = np.linspace(0, 1000, 500)
    q_exp = exponential(t_pred, *popt_exp)
    q_har = harmonic(t_pred, *popt_har)
    q_hyp = hyperbolic(t_pred, *popt_hyp)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(t, q, color='black', label='Actual Data')
    plt.plot(t_pred, q_exp, '--', label='Exponential')
    plt.plot(t_pred, q_har, '-.', label='Harmonic')
    plt.plot(t_pred, q_hyp, ':', label='Hyperbolic')

    plt.xlabel("Time (days)")
    plt.ylabel("Production Rate (STB/day)")
    plt.title("Decline Curve Analysis")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Print parameters
    print("Exponential Model: qi = {:.2f}, D = {:.4f}".format(*popt_exp))
    print("Harmonic Model:    qi = {:.2f}, D = {:.4f}".format(*popt_har))
    print("Hyperbolic Model:  qi = {:.2f}, D = {:.4f}, b = {:.4f}".format(*popt_hyp))
