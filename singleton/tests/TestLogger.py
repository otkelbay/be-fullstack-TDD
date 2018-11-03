import unittest
from pathlib import Path
from ..Logger import Logger


class LoggerTestCase(unittest.TestCase):
    def test_for_equality_of_objects(self):
        """
        Checking if only one object is created
        """
        logger_1 = Logger.get_instance()
        logger_2 = Logger.get_instance()
        self.assertEqual(logger_1, logger_2)

    def test_executing_write(self):
        """
        Checking if log writing works
        """
        logger = Logger.get_instance()
        unique_string = 'qwertyuiopasdfghjklzxcvbnmqwertyuioasdfghjklertygbuhnygbgybgybygbgygybbgy'
        logger.write(unique_string)
        logger.close()
        file = open('log.txt', 'r')
        content = file.read()
        file.close()
        self.assertTrue(unique_string in content)

    def test_function_change_file_name(self):
        """
        Checking if file name of log file changing works
        """
        logger = Logger.get_instance()
        logger.change_file_name('new_file_name.txt')
        unique_string = 'dtfasvdyasdvayusdgbasuydgaysudgadyasdygaysduasdguasdgasybu'
        logger.write(unique_string)
        logger.close()
        file = open('new_file_name.txt', 'r')
        content = file.read()
        file.close()
        self.assertTrue(unique_string in content)

    def test_initialization_of_file(self):
        """
        Checking if file inited
        """
        Logger.get_instance()
        log_file = Path("log.txt")
        self.assertTrue(log_file.is_file())

    def test_function_file_close(self):
        """
        Checking if file closed
        """
        logger = Logger.get_instance()
        logger.close()
        self.assertTrue(logger._file.closed)







if __name__ == '__main__':
    unittest.main()
