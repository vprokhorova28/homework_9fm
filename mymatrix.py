import copy

class MyMatrix:
    def __init__(self, data: list):
        self.__data = copy.deepcopy(data)

    def get_data(self):
        return copy.deepcopy(self.__data)

    def __repr__(self):
        m_n = max(list(filter((lambda x: max(x)),[str(x) for x in self.__data])))
        for i in range(len(self.__data)):
            copy_of_data = copy.deepcopy(self.__data)
            list = [str(x) for x in copy_of_data]
            for j in list:
                if len(j) != m_n:
                    j = ' ' * (m_n - len(j)) + j
            another_list = ' '.join(list)
        m = '\n'.join(another_list)

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
            raise ValueError('Different size')
        else:
            for i in range(len(self.__data)):
                if len(self.__data[i]) != len(other.__data[i]):
                    raise ValueError('Different size')
            m = copy.deepcopy(self.__data)
            for i in range(len(self.__data)):
                for j in range(len(self.__data[i])):
                    m[i][j] += other.__data[i][j]
            return MyMatrix(m)

    def __sub__(self, other):
        if len(self.__data) != len(other.__data):
            raise ValueError('Different size')
        else:
            for i in range(len(self.__data)):
                if len(self.__data[i]) != len(other.__data[i]):
                    raise ValueError('Different size')
            m = copy.deepcopy(self.__data)
            for i in range(len(self.__data)):
                for j in range(len(self.__data[i])):
                    m[i][j] -= other.__data[i][j]
            return MyMatrix(m)

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other
