import csv
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

logger_handler = logging.FileHandler('./log/app.main.log')
logger_handler.setLevel(logging.DEBUG)

logger_format = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s - %(message)s')
logger_handler.setFormatter(logger_format)

logger.addHandler(logger_handler)


def read_currencies():
    try:
        with open('./currencies.csv', 'r', encoding='utf-8-sig') as csvf:
            reader = csv.DictReader(csvf, delimiter=';', quoting=csv.QUOTE_NONE)
            data = [x for x in reader]
    except Exception as e:
        logger.error(f'Cannot read currencies. ({e})')

        return ('Error', str(e))
    else:
        return data


if __name__ == '__main__':
    print(read_currencies())
