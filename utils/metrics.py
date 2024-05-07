import numpy as np

def calculate_accuracy_score(accuracy_percentage):
    #accuracy_percentage = (measured_size / nominal_size) * 100
    score = max(0, 1 - abs((accuracy_percentage - 100) / 100))
    return score

def overall_objective(accuracy_percentage, success_percentage):    
    """
    Calculates the overall objective score combining accuracy and success.
    
    Args:
    measured_size (float): The actual size measured from the printed part.
    nominal_size (float): The intended nominal size of the printed part.
    success_percentage (float): Continuous measure from 0 to 1 of successful printing completion.

    Returns:
    float: Combined objective score, where higher is better.
    """
    # Calculate the accuracy score based on deviation from nominal size
    #accuracy_score = calculate_accuracy_score(accuracy_percentage)
    accuracy_score = np.maximum(0, 1 - abs((accuracy_percentage - 100) / 100))
    # Success percentage is already normalized between 0 and 1
    success_score = success_percentage

    # Weighted sum of accuracy and success
    overall_score = 0.5 * accuracy_score + 0.5 * success_score
    
    return overall_score
