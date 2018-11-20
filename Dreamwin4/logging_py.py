import logging
from logging.handlers import RotatingFileHandler

# creating  a logegr instance
logger = logging.getLogger(__name__)
FORMAT = '%(asctime)s - %(levelname)s - %(lineno)d - %(name)s - %(module)s - %(message)s'
#logging.basicConfig(level=logging.DEBUG, format=FORMAT)

# file handler to log messages into a file
#handler = logging.FileHandler('abc.log', 'w')

handler = RotatingFileHandler('xyz.log', 'w', maxBytes=100, backupCount=4)

formatter = logging.Formatter(FORMAT)
# sett the formatter to handler
handler.setFormatter(formatter)
# add handler to logger instance
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.error('an error may occur')
logger.exception('exception occurs')
logger.warning('warning')
logger.info('implementing logging')
logger.debug('debug message')
#logger.info('rotating handler')


