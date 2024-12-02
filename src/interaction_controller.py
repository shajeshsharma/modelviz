# this module handles the user controls

import sys
from simulation_engine import SimulationEngine
from visualization_manager import VisualizationManager

class InteractionController:
    def __init__(self):
        self.sim_engine = SimulationEngine()
        self.vis_manager = VisualizationManager()

    def get_user_input(self):
        """Retrieve model source from command-line arguments."""
        if len(sys.argv) < 2:
            print("Usage: python main.py <model_path_or_url>")
            sys.exit(1)
        return sys.argv[1]  # Get the file path or URL from command-line arguments

    def run(self):
        model_source = self.get_user_input()  # Call to get user input

        try:
            # Load model and run simulation
            self.sim_engine.load_model(model_source)
            simulation_result = self.sim_engine.run_simulation()

            # Extract data and animate visualization
            time_series = simulation_result[:, 1:]  # Skip time column
            species_names = self.sim_engine.model.getFloatingSpeciesIds()
            self.vis_manager.animate_bar_chart(time_series, species_names)

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

