#Singleton

Singleton - In software engineering,
    the singleton pattern is a software design pattern that restricts
    the instantiation of a class to one object.
    For more information: https://en.wikipedia.org/wiki/Singleton_pattern
    We created class Logger which serves as tool to record
    an information to log file.
    Logger implements Singleton pattern.
    To read more information about logger: https://www.quora.com/What-is-Logging-in-programming 

##Part1 

1) Look at the file Logger.py

2) We write some unit test for  Logger class (look at the file tests/TestLogger.py)

3) Run tests:

        python3 -m unittest tests/TestLogger.py 
    
    You will see that it ran 5 tests and all of them FAILED (failures=5)

4) Now, complete that functions in Logger.py

5) After running tests all of them should be passed.

6) Compare your answer with answers in answers/Logger.py