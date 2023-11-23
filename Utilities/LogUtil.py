import logging
import time
import os


class Logger():
    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        curr_time = time.strftime("%Y-%m-%d")

        # Construct an absolute path for the log file
        log_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Logs'))
        self.LogFileName = os.path.join(log_directory, 'log' + curr_time + '.txt')

        # Create the Logs directory if it doesn't exist
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # "a" to append the logs in same file, "w" to generate new logs and delete old one
        fh = logging.FileHandler(self.LogFileName, mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
