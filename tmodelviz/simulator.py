import tellurium as te

def load_and_simulate(url, start_time, end_time, steps):
    runner = te.loadSBMLModel(url)
    data = runner.simulate(start_time, end_time, steps)
    return runner, data