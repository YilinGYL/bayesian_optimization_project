from bayes_opt import UtilityFunction

def create_utility_function(kind="ucb", kappa=2.576, xi=0.0):
    """
    Creates and returns a utility function object for Bayesian optimization.

    Parameters:
    kind (str): The type of acquisition function to use ("ucb", "ei", or "poi").
    kappa (float): Controls the exploration-exploitation trade-off for "ucb".
    xi (float): Controls the exploration-exploitation trade-off for "ei" and "poi".

    Returns:
    UtilityFunction: Configured utility function for Bayesian optimization.
    """
    utility = UtilityFunction(kind=kind, kappa=kappa, xi=xi)
    return utility
