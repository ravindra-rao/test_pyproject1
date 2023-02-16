'''
Created on Feb. 9, 2023

@author: wearo
'''
from logging import getLogger

print(__name__)  # will print test_pyproject1.utils.db or test_pyproject1.core.engine
logger = getLogger(__name__)
print(id(logger))  # different object for each module; child of root though


def connect():
    logger.info("started")