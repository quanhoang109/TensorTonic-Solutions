import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X = np.array(X, dtype=float)  # ensure numpy array
    y = np.array(y, dtype=float)  # ensure numpy array
    w = np.zeros(X.shape[1])
    b = 0.0
    N = len(y)
    for _ in range(steps):
        ## Forward Pass
        p = _sigmoid(X@w + b)
        ## Gradient
        gradient_w = X.T @ (p - y)/ N
        gradient_b = np.mean(p - y)

        ## Update: 
        w = w - lr * gradient_w
        b = b - lr * gradient_b
    return (w,b)
    pass