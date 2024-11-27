class Counter:
    def __init__(self):
        self.__count = 0

    def increment(self):
        self.__count +=1
    
    @property
    def count(self):
        return self.__count
    
    def reset(self):
        self.__count = 0