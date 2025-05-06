# risk_modeling.py

import numpy as np
import matplotlib.pyplot as plt

class RiskModeling:
    def __init__(self):
        pass

    def run_simulation(self):
        print("Running Monte Carlo simulation for portfolio risk...")
        
        # Simulate random portfolio returns over 1000 iterations
        simulations = np.random.normal(0.05, 0.1, 1000)  # mean return of 5% and std dev of 10%
        
        # Plot the risk distribution
        plt.hist(simulations, bins=30, edgecolor='black')
        plt.title("Monte Carlo Simulation: Portfolio Risk Distribution")
        plt.xlabel("Portfolio Return")
        plt.ylabel("Frequency")
        plt.show()
