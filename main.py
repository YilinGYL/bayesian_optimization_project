# main.py

# Importing the calculate_accuracy_score function from the metrics module in utils package
import os
from utils.metrics import calculate_accuracy_score, overall_objective
from utils.data_processing import load_data, normalize, denormalize, add_normalized_column

def main():
    
    # Define the path to the data directory relative to the current script location
    current_directory = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_directory, "data", "raw", "Exp_log.csv")
    
    # Load Data
    raw_data = load_data(data_path)
    enriched_data = add_normalized_column(raw_data)
    print(enriched_data)

    # Log Data 
    # enriched_data.to_csv(xxxxx)

    







    # Example usage of the calculate_accuracy_score function
    accuracy_percentage = 95  # This might be calculated or provided elsewhere in your code
    print_rate = 0.89
    
    accuracy_score = calculate_accuracy_score(accuracy_percentage)
    
    overall_score = overall_objective(accuracy_score, print_rate)

    print(f"Calculated Score: {overall_score}")

    
    

if __name__ == "__main__":
    main()
