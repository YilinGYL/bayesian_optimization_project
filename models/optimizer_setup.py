# Bayesian Optimizer

from bayes_opt import BayesianOptimization

def initialize_optimizer():
    # Parameter bounds
    pbounds = {
        'x': (0, 1),
        'y': (0, 1),
        'z': (0, 1)
    }

    # Initialize Bayesian Optimization
    optimizer = BayesianOptimization(
        f=None,  # f is None because we don't have a black box function
        pbounds=pbounds,
        verbose=2,
        random_state=1,
        allow_duplicate_points=True
    )
    return optimizer