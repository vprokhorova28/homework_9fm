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

def test_size():
    zero_matrix = MyMatrix([])
    size = zero_matrix.size()
    matrix = MyMatrix([[1, 2], [5, 6], [4, 7]])
    s = matrix.size()
    assert(zero_matrix.size() == (0, 0))
    assert(matrix.size() == (3, 2))

def test_flip_up_down():
    zero_matrix = MyMatrix([])
    matrix = MyMatrix([[1, 2], [5, 6], [4, 7]])
    assert(matrix.flip_up_down().get_data() == [[4, 7], [5, 6], [1, 2]])
    assert(zero_matrix.flip_up_down().get_data() == [])

def test_flip_left_right():
    zero_matrix = MyMatrix([])
    matrix = MyMatrix([[1, 2], [5, 6], [4, 7]])
    assert(matrix.flip_left_right().get_data() == [[2, 1], [6, 5], [7, 4]])
    assert(zero_matrix.flip_left_right().get_data() == [])
    
def test_flipped_up_down():
    zero_matrix = MyMatrix([])
    zero_matrixcopy = zero_matrix.flipped_up_down()
    matrix = MyMatrix([[1, 2], [5, 6], [4, 7]])
    matrix2 = matrix.flipped_up_down()
    assert(matrix2.get_data() == [[4, 7], [5, 6], [1, 2]])
    assert(matrix.get_data() == [[1, 2], [5, 6], [4, 7]])
    assert(zero_matrix.get_data() == [])
    assert(zero_matrixcopy.get_data() == [])

def test_flipped_left_right():
    zero_matrix = MyMatrix([])
    zero_matrixcopy = zero_matrix.flipped_left_right()
    matrix = MyMatrix([[1, 2], [5, 6], [4, 7]])
    matrix2 = matrix.flipped_left_right()
    assert(matrix2.get_data() == [[2, 1], [6, 5], [7, 4]])
    assert(matrix.get_data() == [[1, 2], [5, 6], [4, 7]])
    assert(zero_matrix.get_data() == [])
    assert(zero_matrixcopy.get_data() == [])

def test_transpose():
    zero_matrix = MyMatrix([])
    matrix = MyMatrix([[1, 2], [5, 6], [4, 7]])
    matrix.transpose()
    assert(matrix.size() == (2, 3))
    assert(matrix.get_data() == [[1, 5, 4], [2, 6, 7]])
    assert(zero_matrix.transpose().get_data() == [])


def test_transposed():
    zero_matrix = MyMatrix([])
    zero_matrixcopy = zero_matrix.transposed()
    matrix = MyMatrix([[1, 2], [5, 6], [4, 7]])
    matrix2 = matrix.transposed()
    assert(matrix2.size() == (2, 3))
    assert(matrix2.get_data() == [[1, 5, 4], [2, 6, 7]])
    assert(zero_matrix.get_data() == [])
    assert(zero_matrixcopy.get_data() == [])

def test___setitem__():
    matrix = MyMatrix([[1, 2], [5, 100], [4, 7]])
    matrix[0][1] = 6
    # matrix[1, 1] = 100
    assert(matrix.get_data() == [[1, 6], [5, 100], [4, 7]])
    raise Exception

def test___getitem__():
    matrix = MyMatrix([[1, 2], [5, 6], [4, 7]])
    assert(matrix[0][1] == 2)
    # assert(matrix[1, 1] == 6)
    raise Exception
