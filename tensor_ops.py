
#Array Operations 
#ReLU implementation
def naive_relu(x):
    assert len(x.shape) == 2

    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] = max(x[i, j], 0)
    return x 

matrix = np.array([[5, 78, 2, 34, 0],
                  [6, 79, 3, 35, 1],
                  [7, 80, 4, 36, 2]])
# naive_relu(matrix)


#element-wise addition of two matrices.. can modify to subtraction, mult, etc.
def naive_add(x, y):
    assert len(x.shape) == 2
    assert x.shape == y.shape 
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[i, j]
    return x
    
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])
# naive_add(x, y)


#add a matrix and a vector using broadcasting
def naive_add_matrix_and_vector(x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 1
    assert x.shape[1] == y.shape[0] #number of columns in x matches number of elements in y

    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[j]
    return x

x = np.array([[1, 2, 3],
     [4, 5, 6]])
y = np.array([10, 20, 30])
# naive_add_matrix_and_vector(x, y)


#sum of dot product of two vectors
def naive_dot_product(x, y):
    assert len(x.shape) == 1
    assert len(y.shape) == 1
    assert x.shape[0] == y.shape[0]

    z = 0.
    for i in range(x.shape[0]):
        z += x[i] * y[i]
    return z 

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
# naive_dot_product(x, y)


#dot product of vector and matrix. returns vector result.
def naive_matrix_vector_dot(x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 1
    assert x.shape[1] == y.shape[0]

    z = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i] += x[i, j] * y[j]
    return z 
    
x = np.array([[1, 2, 3],
     [4, 5, 6]])
y = np.array([10, 20, 30])
naive_matrix_vector_dot(x, y)

#-------------------------------------------#

def naive_vector_dot(x, y):
    """
    Computes the dot product of two vectors.

    Parameters:
    x (np.ndarray): A 1-dimensional numpy array.
    y (np.ndarray): A 1-dimensional numpy array.

    Returns:
    float: The dot product of the two vectors.
    
    Raises:
    AssertionError: If either x or y is not a 1-dimensional array.
    """
    assert len(x.shape) == 1
    assert len(y.shape) == 1

    z = 0.
    for i in range(x.shape[0]):
        z += x[i] * y[i]
    return z 

def naive_matrix_dot(x, y):
    """
    Computes the matrix product of two matrices using a naive approach.

    Parameters:
    x (np.ndarray): A 2-dimensional numpy array.
    y (np.ndarray): A 2-dimensional numpy array.

    Returns:
    np.ndarray: The result of the matrix multiplication.
    
    Raises:
    AssertionError: If either x or y is not a 2-dimensional array, 
                    or if the number of columns in x does not equal the number of rows in y.
    """
    assert len(x.shape) == 2
    assert len(y.shape) == 2
    assert x.shape[1] == y.shape[0]

    z = np.zeros((x.shape[0], y.shape[1]))
    for i in range(x.shape[0]):
        for j in range(y.shape[1]):
            row_x = x[i, :]
            column_y = y[:, j]
            z[i, j] = naive_vector_dot(row_x, column_y)

    return z 

if __name__ == "__main__":
    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([[10, 12], [13, 14], [15, 16]])
    final = naive_matrix_dot(x, y)
    print(final)



