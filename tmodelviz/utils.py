import numpy as np

def calculate_rolling_average(concentrations, time, index, window_size):
    start = max(0, index - window_size // 2)
    end = min(len(time), index + window_size // 2 + 1)
    return np.mean(concentrations[start:end], axis=0)

def extract_fluxes(runner, species_names, species_concentrations, index):
    runner.reset()
    for species, conc in zip(species_names, species_concentrations[index]):
        runner[species] = conc
    return runner.getReactionRates(), runner.getReactionIds()
