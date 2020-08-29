from my_logger import get_logger
from util.util_functions import sum_list


logger = get_logger(__name__)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = sum_list(data)
    logger.info('data: {} => result: {}'.format(data, result))
