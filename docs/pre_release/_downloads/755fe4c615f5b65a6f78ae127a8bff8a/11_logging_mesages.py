"""
====================
Logging and debuging
====================

"""
import logging
import spydrnet as sdn

logger = logging.getLogger("spydrnet_logs")

logger.info("This is information")
logger.debug("This is debug message")
logger.warning("This is warning message")

# Turn on logging in file, and set LOG LEVEL
sdn.enable_file_logging(LOG_LEVEL="INFO", filename="execution_log_file")
logger.info("file: This is information")
logger.debug("file: This is debug message")
logger.warning("file: This is warning message")

# Dynamically turn on DEBUG for part of code
logger.handlers[1].setLevel(logging.DEBUG)
logger.info("Dynamic: This is information")
logger.debug("Dynamic: This is debug message")
logger.warning("Dynamic: This is warning message")
logger.handlers[1].setLevel(logging.INFO)

# %%
#
# **Output log file** (*_execution_log_file_spydrnet.log*)
#
# .. literalinclude:: ../../../examples/basic/_execution_log_file_spydrnet.log
#
