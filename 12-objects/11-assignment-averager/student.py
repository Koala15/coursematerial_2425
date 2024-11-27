class Averager:
    def __init__(self):
        self.__value = 0
        self.__count = 0

    def add(self, value):
        if isinstance(value, int):
            self.__value += value
            self.__count += 1
        else:
            raise ValueError()

    def average(self):
        if (self.__count == 0):
            return 0
        return (self.__value / self.__count)

    def reset(self):
        self.__value = 0
        self.__count = 0