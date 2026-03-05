import sys
from visa_project.logger import logging
# visa_project/logger/__init__.py
from visa_project.exception import USvisaException
from visa_project.pipeline.training_pipeline import TrainPipeline
'''
This guarantees:

Same logging config everywhere

Centralized logging setup

No duplicate configuration

'''
logging.info("My own created custom log")

try:
    obj = TrainPipeline()
    obj.run_pipeline()
    logging.info("pipeline finished successfully")
except Exception as e:
    # print("Exception object:", e)
    # print("sys.exc_info():", sys.exc_info())
    raise USvisaException(e, sys)