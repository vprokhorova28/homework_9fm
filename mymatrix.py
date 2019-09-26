import copy


class MyMatrix:
    def __init__(self, data: list):
        self.__data = copy.deepcopy(data)

    def __repr__(self):
        for i in range(len(self.__data)):
            copy_of_data = copy.deepcopy(self.__data)
            list = [str(x) for x in copy_of_data]
            for j in list:
                if len(j) != 4:
                    j = ' ' * (4 - len(j)) + j
            another_list = ' '.join(list)
        m = '\n'.join(another_list)
        return m

    def size(self):
        return (len(self.__data), len(self.__data[0]))

    def flip_up_down(self):
        self.__data.reverse()
        return self.__data

    def flip_left_right(self):
        [x.reverse() for x in self.__data]
        return self.__data

    def flipped_up_down(self):
        return list(reversed(self.__data))

    def flipped_left_right(self):
        return [list(reversed(x)) for x in self.__data]

    def transpose(self):
        self.__data = list(zip(*self.__data))
        return self.__data

    def transposed(self):
        return list(zip(*self.__data))

    def __add__(self, other):
        if len(self.__data) != len(other.__data):
            raise ValueError('Матрицы разного размера')
        else:
            for i in range(len(self.__data)):
                if len(self.__data[i]) != len(other.__data[i]):
                    raise ValueError('Матрицы разного размера')
            m = copy.deepcopy(self.__data)
            for i in range(len(self.__data)):
                for j in range(len(self.__data[i])):
                    m[i][j] += other.__data[i][j]
            return MyMatrix(m)

    def __sub__(self, other):
        if len(self.__data) != len(other.__data):
            raise ValueError('Матрицы разного размера')
        else:
            for i in range(len(self.__data)):
                if len(self.__data[i]) != len(other.__data[i]):
                    raise ValueError('Матрицы разного размера')
            m = copy.deepcopy(self.__data)
            for i in range(len(self.__data)):
                for j in range(len(self.__data[i])):
                    m[i][j] -= other.__data[i][j]
            return MyMatrix(m)

    def __iadd__(self, other):
        if len(self.__data) != len(other.__data):
            raise ValueError('Матрицы разного размера')
        else:
            for i in range(len(self.__data)):
                if len(self.__data[i]) != len(other.__data[i]):
                    raise ValueError('Матрицы разного размера')
            for i in range(len(self.__data)):
                for j in range(len(self.__data[i])):
                    self.__data[i][j] += other.__data[i][j]
        return MyMatrix(self.__data)

    def __isub__(self, other):
        if len(self.__data) != len(other.__data):
            raise ValueError('Матрицы разного размера')
        else:
            for i in range(len(self.__data)):
                if len(self.__data[i]) != len(other.__data[i]):
                    raise ValueError('Матрицы разного размера')
            for i in range(len(self.__data)):
                for j in range(len(self.__data[i])):
                    self.__data[i][j] -= other.__data[i][j]
        return MyMatrix(self.__data)
