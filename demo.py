import sys
from visa_project.logger import logging
# visa_project/logger/__init__.py
from visa_project.exception import USvisaException

'''
This guarantees:

Same logging config everywhere

Centralized logging setup

No duplicate configuration

'''
logging.info("My own created custom log")

try:
    1 / 0
except Exception as e:
    # print("Exception object:", e)
    # print("sys.exc_info():", sys.exc_info())
    raise USvisaException(e, sys)