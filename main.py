# main.py

# Importing the calculate_accuracy_score function from the metrics module in utils package
from utils.metrics import calculate_accuracy_score, overall_objective
from utils.data_processing import normalize, denormalize
def main():
    # Example usage of the calculate_accuracy_score function
    accuracy_percentage = 95  # This might be calculated or provided elsewhere in your code
    print_rate = 0.89
    
    accuracy_score = calculate_accuracy_score(accuracy_percentage)
    
    overall_score = overall_objective(accuracy_score, print_rate)

    print(f"Calculated Score: {overall_score}")

if __name__ == "__main__":
    main()
