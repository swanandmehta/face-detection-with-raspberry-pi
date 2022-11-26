import logging
import sys

logging.basicConfig(filename='./output/system.log', filemode='w', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


def info(message):
    logging.info(message)
