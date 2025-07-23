# dca.py file

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, OptimizeWarning
import warnings

# Decline curve models
def exponential(t, qi, D):
    return qi * np.exp(-D * t)

def harmonic(t, qi, D):
    return qi / (1 + D * t)

def hyperbolic(t, qi, D, b):
    return qi / np.power(1 + b * D * t, 1 / b)

def perform_dca(file_path):
    df = pd.read_csv(file_path)
    
    # Ensure column names are correct
    if 'time_days' not in df.columns or 'production_rate' not in df.columns:
        raise ValueError("CSV file must contain 'time_days' and 'production_rate' columns.")
    
    t = df['time_days'].values
    q = df['production_rate'].values

    # Exponential model
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", OptimizeWarning)
        try:
            popt_exp, _ = curve_fit(exponential, t, q, bounds=(0, np.inf), maxfev=10000)
            print("Exponential Model: qi = {:.2f}, D = {:.4f}".format(*popt_exp))
        except Exception as e:
            print("Exponential Model: Fit failed —", str(e))

    # Harmonic model
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", OptimizeWarning)
        try:
            popt_har, _ = curve_fit(harmonic, t, q, bounds=(0, np.inf), maxfev=10000)
            print("Harmonic Model:    qi = {:.2f}, D = {:.4f}".format(*popt_har))
        except Exception as e:
            print("Harmonic Model: Fit failed —", str(e))

    # Hyperbolic model
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", OptimizeWarning)
        try:
            popt_hyp, _ = curve_fit(hyperbolic, t, q, bounds=([0, 0, 0], [np.inf, 1, 1]), maxfev=10000)
            print("Hyperbolic Model:  qi = {:.2f}, D = {:.4f}, b = {:.4f}".format(*popt_hyp))
        except Exception as e:
            print("Hyperbolic Model: Fit failed —", str(e))

    # Plotting the decline models
    t_fit = np.linspace(t.min(), t.max(), 100)

    plt.figure(figsize=(10, 6))
    plt.scatter(t, q, label='Observed', color='black')

    try:
        plt.plot(t_fit, exponential(t_fit, *popt_exp), label='Exponential', linestyle='--')
    except:
        pass

    try:
        plt.plot(t_fit, harmonic(t_fit, *popt_har), label='Harmonic', linestyle='-.')
    except:
        pass

    try:
        plt.plot(t_fit, hyperbolic(t_fit, *popt_hyp), label='Hyperbolic', linestyle=':')
    except:
        pass

    plt.xlabel('Time (days)')
    plt.ylabel('Production Rate')
    plt.title('Decline Curve Analysis')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
