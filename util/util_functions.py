from functools import reduce

from my_logger import get_logger

logger = get_logger(__name__)


def summation(a, b):
    logger.info('a: {}, b: {}'.format(a, b))
    return a + b


def sum_list(data):
    return reduce(summation, data)
