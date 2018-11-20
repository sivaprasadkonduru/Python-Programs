import logging

from logging.handlers import RotatingFileHandler

print(__name__)

format = logging.Formatter('%(asctime)s - %(levelno)s - %(levelname)s - %(module)s - %(message)s - %(lineno)s - %(pathname)s - %(name)s')
#logging.basicConfig(format=format, level=logging.WARNING)
logger = logging.getLogger(__name__)  # created logger instance
logger.setLevel(logging.DEBUG)  # setting logger level

# filehandler
'''file_handler = logging.FileHandler('abc.log') # creating file
file_handler.setFormatter(format) # setting format for file handler
logger.addHandler(file_handler)  # adding file handler to logger instance'''

# stream handler
console = logging.StreamHandler()
console.setFormatter(format)
console.setLevel(level=logging.INFO)
logger.addHandler(console)

#rotating filr handler
rotate_handler = RotatingFileHandler('rlog.log', maxBytes=300, backupCount=3)
rotate_handler.setFormatter(format)
rotate_handler.setLevel(level=logging.Error)
logger.addHandler(rotate_handler)


logger.info("Hello python")
logger.debug("Welcome python.")
'''logger.error("error message")
logger.exception("exception occurs")
logger.warning("warning message")
logger.info("Hello Dreamwin")
logger.debug("Debug info")'''


if __name__ == "__main__":
    print("hello")