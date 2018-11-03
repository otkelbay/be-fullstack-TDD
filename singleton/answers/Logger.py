import datetime

"""
We imported module datetime to use it in function write()
"""


class Logger:
    """
    We created class Logger which serves as tool to record
    an information to log file.
    Logger implements Singleton pattern.
    To read more information about logger: https://www.quora.com/What-is-Logging-in-programming
    Singleton - In software engineering,
    the singleton pattern is a software design pattern that restricts
    the instantiation of a class to one object.
    For more information: https://en.wikipedia.org/wiki/Singleton_pattern
    """

    _instance = None
    """
        _instance: Variable for our Logger instance, for now it is declared as None.
    """
    _file = None
    """
        _file: Variable for our file stream, python core 'open()' function is used. 
    """

    """
    Decorator function which transforms a method into a static method.
    For more information: https://docs.python.org/3/library/functions.html#staticmethod
    """

    @staticmethod
    def get_instance():
        """
        Called to get instance of Class;
        Returns an instance of our Logger,
        firstly checks if our instance is empty(none),
        if so creates , else (if our instance already created) returns instance
        :return: Logger
        """
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def __init__(self):
        """
        Magic function __init__: Called when object of class created.
        Initializes file name -- function initialize_file called with value log.txt as parameter file_name
        File name by default - log.txt
        """
        self.initialize_file('log.txt')

    def initialize_file(self, file_name):
        """
        Initializes _file attribute to file stream returned by open() function.
        We invoke open function with arguments file_name  and mode( with value 'w'(which means write))
        Read more about open() function: https://docs.python.org/3/tutorial/inputoutput.html
        :param file_name: Name of file where logs must be written
        :return: void
        """
        self._file = open(file_name, 'w')

    def change_file_name(self, file_name):
        """
        Function that changes name of file where logs must be written.
        To do this it calls function initialize_file with argument file_name
        :param file_name: Name of file where logs must be written
        :return: void
        """
        self.initialize_file(file_name)

    def write(self, text):
        """
        Function that writes text into log file.
        To do this it calls write function of our stream stored in _file attribute with argument log.
        Log is concatenated string which contains "current date + text + new line"
        :param text: Text which must be written  to log file
        :return:
        """
        log = str(datetime.datetime.now()) + ' : ' + text + '\n'
        self._file.write(log)

    def close(self):
        """
        Function which closes our _file stream
        To do this it calls close function of stream stored in _file attribute.
        :return:void
        """
        self._file.close()


