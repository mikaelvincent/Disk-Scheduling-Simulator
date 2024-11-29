import logging

def setup_logging():
    """
    Set up the logging configuration for the Disk Scheduling Simulator.
    Logs are displayed on the command-line interface with detailed information.
    """
    logger = logging.getLogger('DiskSchedulingSimulator')
    logger.setLevel(logging.DEBUG)

    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    if not logger.handlers:
        logger.addHandler(ch)

    return logger
