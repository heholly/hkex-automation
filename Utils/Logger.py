# File Name: Logger
# Author: Karthick Dhakshinamoorthy
# Python Version: 3.5.4

import logging, coloredlogs

# logging.basicConfig(level=logging.INFO)
coloredlogs.install(level=logging.INFO, fmt='%(levelname)s %(message)s')
logger = logging.getLogger(__name__)



