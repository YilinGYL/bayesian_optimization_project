
from models.optimizer_setup import initialize_optimizer
from utils.optimization_helper import create_utility_function

def optimize_process():
    optimizer = initialize_optimizer()
    utility = create_utility_function(kind="ucb", kappa=10, xi=0)

    # Example of using the optimizer with the utility function
    next_point = optimizer.suggest(utility)
    # result = evaluate_function_at(next_point)  # You would define this evaluation function
    # Need to key in a new results from experiment
    optimizer.register(params=next_point, target=result)

    return optimizer.max

def main():
    optimal_result = optimize_process()
    print(f"Optimal result: {optimal_result}")

if __name__ == "__main__":
    main()
