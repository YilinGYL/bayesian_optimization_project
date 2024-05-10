import json
import os

def log_experiment(params, result=None):
    """
    Logs the experiment parameters and results to a JSON file.

    Parameters:
    params (dict): The parameters suggested by the optimizer.
    result (float, optional): The result of the experiment, if available.
    """
    log_entry = {'params': params, 'result': result}
    file_path = 'experiment_logs.json'

    # Check if the file exists, read existing data and append to it
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            logs = json.load(file)
    else:
        logs = []

    logs.append(log_entry)

    with open(file_path, 'w') as file:
        json.dump(logs, file, indent=4)

    print("Logged experiment:", log_entry)
