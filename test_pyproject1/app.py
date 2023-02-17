'''
Created on Feb. 9, 2023

@author: wearo
'''
import logging
import sys

# from test_pyproject1.core import engine
# from test_pyproject1.utils import db

from core import engine
from utils import db


logger = logging.getLogger()
logger.setLevel(logging.INFO)
stdout = logging.StreamHandler(sys.stdout)
stdout.setFormatter(logging.Formatter("%(name)s: %(message)s"))
logger.addHandler(stdout)


def run():
    db.connect()
    engine.connect()


run()