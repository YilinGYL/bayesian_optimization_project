# Functions for normalizing the parameters for effectively explore the searching space
import pandas as pd
from .metrics import overall_objective

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df
    
# def clean_data(data):
#     # Clean raw data (e.g., remove missing values)
#     pass


def normalize(value, min_bound, max_bound):
    return (value - min_bound) / (max_bound - min_bound)

#def normalize_parameters(params, bounds):
    normalized_params = {}
    for key in params:
        normalized_params['normalized_' + key] = normalize(params[key], bounds[key][0], bounds[key][1])
    return normalized_params

def denormalize(normalized_value, min_bound, max_bound):
    return normalized_value * (max_bound - min_bound) + min_bound



def add_normalized_column(df):
    df['base_t_n'] = normalize (df['base_t'], df['base_t_min'], df['base_t_max'])
    df['part_t_n'] = normalize (df['part_t'], df['part_t_min'], df['part_t_max'])
    df['layer_th_n'] = normalize (df['layer_th'], df['layer_t_min'], df['layer_t_max'])
    df['overall_objective'] = overall_objective(df['accuracy'], df['success_r'])
    return df
