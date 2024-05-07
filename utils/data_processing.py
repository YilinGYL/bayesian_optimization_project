# Functions for normalizing the parameters for effectively explore the searching space
def normalize(value, min_bound, max_bound):
    return (value - min_bound) / (max_bound - min_bound)

#def normalize_parameters(params, bounds):
    normalized_params = {}
    for key in params:
        normalized_params['normalized_' + key] = normalize(params[key], bounds[key][0], bounds[key][1])
    return normalized_params

def denormalize(normalized_value, min_bound, max_bound):
    return normalized_value * (max_bound - min_bound) + min_bound
