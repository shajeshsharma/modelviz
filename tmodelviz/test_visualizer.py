import unittest
from unittest.mock import patch, MagicMock
from tmodelviz.visualizer import plot_interactive_visualization

class TestPlotInteractiveVisualization(unittest.TestCase):

    @patch('tmodelviz.visualizer.load_and_simulate')
    @patch('tmodelviz.visualizer.calculate_rolling_average')
    @patch('tmodelviz.visualizer.extract_fluxes')
    @patch('tmodelviz.visualizer.plt.show')
    def test_plot_interactive_visualization(self, mock_show, mock_extract_fluxes, mock_calculate_rolling_average, mock_load_and_simulate):
        # Mock the return values of the imported functions
        mock_load_and_simulate.return_value = (MagicMock(), MagicMock())
        mock_load_and_simulate.return_value[1][:, 0] = [0, 1, 2, 3, 4, 5]
        mock_load_and_simulate.return_value[1][:, 1:] = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
        mock_load_and_simulate.return_value[0].getFloatingSpeciesIds.return_value = ['A', 'B']
        mock_calculate_rolling_average.return_value = [1, 2]
        mock_extract_fluxes.return_value = ([0.1, 0.2], ['R1', 'R2'])

        # Call the function to test
        plot_interactive_visualization('dummy_url', start_time=0, end_time=5, steps=5)

        # Check if the mocked functions were called
        mock_load_and_simulate.assert_called_once_with('dummy_url', 0, 5, 5)
        mock_calculate_rolling_average.assert_called()
        mock_extract_fluxes.assert_called()
        mock_show.assert_called()

if __name__ == '__main__':
    unittest.main()