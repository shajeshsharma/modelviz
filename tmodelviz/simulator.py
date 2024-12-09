# simulator.py

import tellurium as te

def load_and_simulate(url, start_time, end_time, steps):
    """
    Loads an SBML model from the given URL and simulates it.
    
    Args:
        url (str): Path to the SBML file or URL.
        start_time (float): Start time for the simulation.
        end_time (float): End time for the simulation.
        steps (int): Number of steps in the simulation.
    
    Returns:
        tuple: A tuple containing the runner object and simulation data.
    """
    runner = te.loadSBMLModel(url)
    data = runner.simulate(start_time, end_time, steps)
    return runner, data
