import csv
import os

def log_experiment_to_csv(params, result=None, file_path='experiment_logs.csv'):
    """
    Logs experiment parameters and results to a CSV file.

    Parameters:
    params (dict): The parameters used in the experiment.
    result (float, optional): The result of the experiment.
    file_path (str): Path to the CSV file where logs are saved.
    """
    # Check if file exists to determine if we need to write headers
    file_exists = os.path.isfile(file_path)
    
    # Open the file in append mode ('a')
    with open(file_path, mode='a', newline='') as file:
        fieldnames = ['experiment_id'] + list(params.keys()) + ['result']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write header only if file does not exist
        if not file_exists:
            writer.writeheader()
        
        # Prepare the row to be written
        log_entry = {**params, 'result': result}
        
        # Optionally add an experiment ID if needed
        if not file_exists:
            log_entry['experiment_id'] = 1
        else:
            # Read the last experiment ID and increment it
            with open(file_path, mode='r', newline='') as read_file:
                last_row = list(csv.DictReader(read_file))[-1]
                log_entry['experiment_id'] = int(last_row['experiment_id']) + 1
        
        # Write the log entry to the CSV
        writer.writerow(log_entry)

    print("Logged experiment to CSV:", log_entry)
