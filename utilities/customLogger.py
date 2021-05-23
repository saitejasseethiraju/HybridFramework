import logging
import os
import sys


class LogGen:

    @staticmethod
    def loggen():
        filename = "D://python//HybridFramework//Logs//automation.log"
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(filename=filename, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # stdout_handler = logging.StreamHandler(sys.stdout)
        # logger.addHandler(stdout_handler)
        return logger

# class LogGen:
#
#     @staticmethod
#     def loggen():
#         logger = logging.getLogger()
#         fhandler = logging.FileHandler(filename="D://python//HybridFramework//Logs//automation.log", mode='a')
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         fhandler.setFormatter(formatter)
#         logger.addHandler(fhandler)
#         logger.setLevel(logging.INFO)
#         return logger
