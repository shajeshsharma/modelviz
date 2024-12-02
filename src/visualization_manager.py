# this module handles visualizations

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class VisualizationManager:
    def plot_bar_chart(self, data, species_names):
        """Plot a static bar chart for the given data."""
        plt.bar(species_names, data)
        plt.xlabel("Species")
        plt.ylabel("Concentration")
        plt.show()

    def animate_bar_chart(self, time_series, species_names, interval=200):
        """Create an animated bar chart."""
        fig, ax = plt.subplots()
        bars = ax.bar(species_names, time_series[0])
        
        def update(frame):
            for bar, height in zip(bars, time_series[frame]):
                bar.set_height(height)
            return bars

        ani = FuncAnimation(fig, update, frames=len(time_series), interval=interval, blit=True)
        plt.show()
