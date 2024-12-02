from simulation_engine import SimulationEngine
from visualization_manager import VisualizationManager
from interaction_controller import InteractionController

sim_engine = SimulationEngine()
vis_manager = VisualizationManager()
interaction_ctrl = InteractionController()

file_path = interaction_ctrl.get_user_input()
sim_engine.load_model(file_path)
result = sim_engine.run_simulation()
vis_manager.animate_bar_chart(result[:, 1:], ["Species1", "Species2", "Species3"])
