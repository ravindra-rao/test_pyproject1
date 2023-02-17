'''
Created on Feb. 9, 2023

@author: wearo
'''
import logging
import sys

# from test_pyproject1.core import engine
# from test_pyproject1.utils import db
'''
We can use either the above or the below
In eclipse, mypy gives some error for the below
But the below runs fine in both eclipse and gitbash
But the above runs only in eclipse and not in gitbash
'''
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