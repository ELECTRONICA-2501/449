import numpy as np
import easynn as nn

# Create a numpy array of 10 rows and 5 columns.
# Set the element at row i and column j to be i+j.
def Q1():
    return np.fromfunction(lambda i, j:j+i, (10,5))

# Add two numpy arrays together.
def Q2(a, b):
    return a+b

# Multiply two 2D numpy arrays using matrix multiplication.
def Q3(a, b):
    return np.dot(a, b)

# For each row of a 2D numpy array, find the column index
# with the maximum element. Return all these column indices.
def Q4(a):
    return np.argmax(a, axis = 1)

# Solve Ax = b.
def Q5(A, b):
    return np.linalg.solve(A,b)

# Return an EasyNN expression for a+b.
def Q6():
    a = nn.Input("a")
    b = nn.Input("b")
    return a+b

# Return an EasyNN expression for a+b*c.
def Q7():
    a = nn.Input("a")
    b = nn.Input("b")
    c = nn.Input("c")
    return a+b*c

# Given A and b, return an EasyNN expression for Ax+b.
def Q8(A, b):
    x = nn.Input("x")
    A = nn.Const(A)
    b = nn.Const(b)
    c = A*x+b
    return c

# Given n, return an EasyNN expression for x**n.
def Q9(n):
    x = nn.Input("x")
    result = x
    for _ in range(n-1):
        result = result*x
    return result

# Return an EasyNN expression to compute
# the element-wise absolute value |x|.
def Q10():
    x = nn.Input("x")
    relu_layer = nn.ReLU()
    relu_x = relu_layer(x)
    relu_neg_x = relu_layer(-x)
    abs_x = relu_x + relu_neg_x
    return abs_x
