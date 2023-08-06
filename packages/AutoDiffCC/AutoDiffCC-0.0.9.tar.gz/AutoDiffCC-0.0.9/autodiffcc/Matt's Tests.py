from autodiffcc.solver import solver
from autodiffcc.ADmath import sin
import inspect
import numpy as np
from autodiffcc.root import root

# def my_soe(x, y):
#     return 2 * x + y - 0, sin(y) - 0.5

# print(solver(my_soe, start=0, method='newton-raphson'))

def lhs(x, y):
    return 2 * x + y, y + 1

def rhs(x,y):
    return 0, 3

def combine_lhs_rhs(lhs, rhs):
    if inspect.signature(lhs).parameters.keys() != inspect.signature(rhs).parameters.keys():
        raise KeyError("Function signatures for LHS and RHS do not match.")
    vars = list(inspect.signature(lhs).parameters.keys())
    print(vars)
    def combined(vars):
        return np.array(lhs(vars)) - np.array(rhs(vars))
    vars = list(inspect.signature(combined).parameters.keys())
    print(vars)
    return combined

# print(zero(lhs, rhs, x=1, y=2))

def test_func(x,y):
    return np.sin(x), np.sin(y)


combined2 = combine_lhs_rhs(lhs, rhs)
# print(combined2(x=1, y=2))

# print(solver(lhs, rhs, start=0, method='newton-raphson', x=1, y=2))
print(root(function=combine_lhs_rhs(lhs,rhs), start=0, method='newton-raphson', threshold=1e-6))