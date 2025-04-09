
"""Visualization Module - Data Visualization Dashboards"""

import matplotlib.pyplot as plt
import pandas as pd

def generate_heatmap(data):
    """Generate a heatmap from sensor data"""
    df = pd.DataFrame(data)
    plt.imshow(df, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.title("Heatmap of Sensor Data")
    plt.show()
