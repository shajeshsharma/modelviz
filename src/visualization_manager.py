# this module handles visualizations

import matplotlib.pyplot as plt
import numpy as np

class VisualizationManager:
    def animate_bar_chart(self, time_series, species_names):
        # Ensure the species_names match the number of species in time_series
        if len(species_names) != time_series.shape[1]:
            raise ValueError(f"Number of species names ({len(species_names)}) does not match number of time series columns ({time_series.shape[1]})")
        
        # Plotting the first time point (you can change this to any specific time step)
        fig, ax = plt.subplots()
        bars = ax.bar(species_names, time_series[0])  # time_series[0] is the first time step
        
        ax.set_xlabel('Species')
        ax.set_ylabel('Concentration')
        ax.set_title('Concentration of Species at Time 0')

        plt.show()
