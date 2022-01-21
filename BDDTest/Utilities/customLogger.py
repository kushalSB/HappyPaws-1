import logging.handlers
import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='BDDTest/Logs/appsLogs.log',
        format = '%(asctime)s -%(message)s',
        datefmt = ' %d-%b-%y %H:%M:%S ', filemode= 'w')
        rotate_file = logging.handlers.RotatingFileHandler(
            'BDDTest/Logs/appsLogs.log', maxBytes = 1024*1024*20,
            backupCount = 3
        )

        logger = logger.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger
