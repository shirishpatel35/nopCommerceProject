import inspect
import logging


class LogGen:
    @staticmethod
    # def loggen():
    #     logging.basicConfig(filename=r"C:\Users\DELL\PycharmProjects\nopCommerceProject\Logs\automation.txt",
    #                         format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    #     logger=logging.getLogger()
    #     logger.setLevel(logging.INFO)
    #     return logger

    def getLogger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('.//Logs//logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger