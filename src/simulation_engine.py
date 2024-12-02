# this module handles simulations

import tellurium as te
import requests

class SimulationEngine:
    def __init__(self):
        self.model = None

    def load_model(self, source):
        """Load a model from a file path or URL."""
        if source.startswith("http://") or source.startswith("https://"):
            file_path = self._download_model(source)
        else:
            file_path = source

        self.model = te.loadSBMLModel(file_path)

    def _download_model(self, url):
        """Download an SBML model from a URL and save it locally."""
        filename = url.split("?filename=")[-1] if "?filename=" in url else url.split("/")[-1]
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            return filename
        else:
            raise Exception(f"Failed to download model: HTTP {response.status_code}")

    def run_simulation(self, start=0, end=100, steps=100):
        """Run the simulation and return the results."""
        if self.model is None:
            raise Exception("No model loaded. Use load_model() first.")
        return self.model.simulate(start, end, steps)