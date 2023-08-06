import numpy as np
from autodiffcc.core import AD, differentiate

def _norm(vector):
    """Returns the absolute value norm of the input vector

    INPUTS
    =======
    vector: numpy array or list-like

    RETURNS
    ========
    the absolute value norm of vector

    EXAMPLES
    =========
    >>> x = np.array([1,2,3])
    >>> _norm(x)
    6.
    """
    return np.sum(np.abs(vector))

def _newton_raphson(function, x_start, y_start, threshold=1e-8, max_iter=2000):
    if isinstance(x_start, AD):
        x_curr = x_start.val
    else:
        x_curr = x_start
    if isinstance(y_start, AD):
        y_curr = y_start.val
    else:
        y_curr = y_start
    jacobian = differentiate(function)
    curr_array = np.array([x_curr, y_curr])
    for i in range(max_iter):
        x_curr, y_curr = curr_array
        val = np.array(function(x_curr, y_curr))
        der = jacobian(x=x_curr, y=y_curr)
        next_array = curr_array - np.matmul(np.linalg.pinv(der), val)
        if np.sum(np.abs(function(next_array[0], next_array[1]))) < threshold:
            return next_array
        curr_array = next_array
    raise Exception("")


def root(function, start, method, threshold=1e-6):
    """Returns the root of the function found using the specified method

    INPUTS
    =======
    function: a function using ADmath methods
    start: the starting point of the root-finding method
    method: the method to do root-finding   #TODO: add list of possible methods
    threshold: the minimum threshold for finding a root
    max_iter: maximum number of iterations that algorithm will look for before quitting
        - in case the function has no roots

    RETURNS
    ========
    the root of the function found using the specified method

    EXAMPLES
    =========
    >>> x = AD(val = 3, der = 1)
    >>> 2 ** x
    (8.0, 5.54517744)
    """
    if method.lower() in ['newton', 'newton-raphson', 'n-r']:
        return _newton_raphson(function, start, threshold)