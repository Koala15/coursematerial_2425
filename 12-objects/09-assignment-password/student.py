class Password:
    def __init__(self, pw):
        self.__password  = pw
    
    def verify(self, str):
        return self.__password  == str