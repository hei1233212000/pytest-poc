from functools import reduce
import logging


def summation(a, b):
    logging.info('a: {}, b: {}'.format(a, b))
    return a + b


def sum_list(data):
    return reduce(summation, data)
