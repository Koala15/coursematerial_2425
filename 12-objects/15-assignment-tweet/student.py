class Tweet:
    def __init__(self, message, max_length):
        if max_length < 1:
            raise ValueError()
        
        self.__message = message
        self.__max_length = max_length
        self.__truncate_message()

    def __truncate_message(self):
        if (len(self.__message) > self.__max_length):
            self.__message = self.__message[0:self.__max_length]
        else:
            self.__message = self.__message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, new_message):
        self.__message = new_message
        self.__truncate_message()

    @property
    def max_length(self):
        return self.__max_length

    @max_length.setter
    def max_length(self, new_length):
        if new_length < 1:
            raise ValueError()
        self.__max_length = new_length
        self.__truncate_message()
