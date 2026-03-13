import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    a = 1/ (1 + np.exp(-np.asarray(x)) )
    return a
    pass