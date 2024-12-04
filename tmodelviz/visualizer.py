import matplotlib.pyplot as plt
from ipywidgets import FloatSlider, Play, jslink, interact, HBox
from IPython.display import display
from utils import calculate_rolling_average, extract_fluxes

def plot_interactive_visualization(url, start_time=0, end_time=10, steps=100):
    from simulator import load_and_simulate

    runner, data = load_and_simulate(url, start_time, end_time, steps)
    time = data[:, 0]
    species_names = runner.getFloatingSpeciesIds()
    species_concentrations = data[:, 1:]
    prev_timestep = [0]

    def plot_bars(timestep):
        plt.figure(figsize=(12, 8))

        current_index = (abs(time - timestep)).argmin()
        previous_index = (abs(time - prev_timestep[0])).argmin()

        current_concentrations = species_concentrations[current_index]
        previous_concentrations = species_concentrations[previous_index]

        differences = (
            current_concentrations - previous_concentrations
            if timestep > prev_timestep[0]
            else previous_concentrations - current_concentrations
        )
        rolling_average = calculate_rolling_average(
            species_concentrations, time, current_index, window_size=10
        )
        fluxes, reaction_names = extract_fluxes(
            runner, species_names, species_concentrations, current_index
        )

        prev_timestep[0] = timestep

        plt.subplot(2, 2, 1)
        plt.bar(species_names, current_concentrations, color="skyblue")
        plt.title(f"Species Concentrations at Time = {timestep:.2f}s")
        plt.ylabel("Concentration")
        plt.xticks(rotation=45)

        plt.subplot(2, 2, 2)
        plt.bar(species_names, differences, color="lightcoral")
        plt.title("Concentration Changes")
        plt.ylabel("Difference")
        plt.xticks(rotation=45)

        plt.subplot(2, 2, 3)
        plt.bar(species_names, rolling_average, color="mediumseagreen")
        plt.title("Rolling Average")
        plt.ylabel("Average")
        plt.xticks(rotation=45)

        plt.subplot(2, 2, 4)
        plt.bar(reaction_names, fluxes, color="gold", alpha=0.7)
        plt.title("Reaction Fluxes")
        plt.ylabel("Flux")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

    slider = FloatSlider(min=start_time, max=end_time, step=(end_time - start_time) / steps, description="Time (s)")
    play = Play(value=0, min=start_time, max=end_time, step=1, interval=250)
    jslink((play, "value"), (slider, "value"))

    interact(plot_bars, timestep=slider)
    display(HBox([play]))