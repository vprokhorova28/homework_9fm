from mymatrix import MyMatrix

def test___add__():
    matrix = MyMatrix([[1, 2], [5, 6], [4, 7]])
    matrix1 = MyMatrix([[1, 2], [5, 6], [4, 1]])
    matrixsum = matrix + matrix1
    assert(matrix.get_data() == [[1, 2], [5, 6], [4, 7]])
    assert(matrix1.get_data() == [[1, 2], [5, 6], [4, 1]])
    assert(matrixsum.get_data() == [[2, 4], [10, 12], [8, 8]])

def test___sub__():
    matrix = MyMatrix([[1, 2], [5, 6], [4, 7]])
    matrix1 = MyMatrix([[1, 2], [5, 6], [4, 1]])
    matrixsum = matrix - matrix1
    assert(matrix.get_data() == [[1, 2], [5, 6], [4, 7]])
    assert(matrix1.get_data() == [[1, 2], [5, 6], [4, 1]])
    assert(matrixsum.get_data() == [[0, 0], [0, 0], [0, 6]])

def test___iadd__():
    matrix = MyMatrix([[1, 2], [5, 6], [4, 7]])
    matrix1 = MyMatrix([[1, 2], [5, 6], [4, 1]])
    matrix += matrix1
    assert(matrix.get_data() == [[2, 4], [10, 12], [8, 8]])
    assert(matrix1.get_data() == [[1, 2], [5, 6], [4, 1]])

def test___isub__():
    matrix = MyMatrix([[1, 2], [5, 6], [4, 7]])
    matrix1 = MyMatrix([[1, 2], [5, 6], [4, 1]])
    matrix -= matrix1
    assert(matrix.get_data() == [[0, 0], [0, 0], [0, 6]])
    assert(matrix1.get_data() == [[1, 2], [5, 6], [4, 1]])
