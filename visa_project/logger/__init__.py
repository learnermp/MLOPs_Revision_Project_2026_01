import logging # This is prebuilt module, no need to install.
import os
from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

log_dir_path = os.path.join(from_root(), log_dir)

os.makedirs(log_dir_path, exist_ok=True)

logs_path = os.path.join(log_dir_path, LOG_FILE)

# basicConfig() configures the root logger.

logging.basicConfig(  
    filename = logs_path,
    format = "[%(asctime)s] %(name)s - %(levelname)s -%(message)s",
    level= logging.DEBUG
)
