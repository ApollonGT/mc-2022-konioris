from logging import getLogger, INFO, FileHandler, Formatter

def get_logger(filename = 'log'):
    logger = getLogger(__name__)
    logger.setLevel(INFO)
    handler = FileHandler(filename =f'{filename}.txt')
    handler.setFormatter(Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    return logger

logger = get_logger()