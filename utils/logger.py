import logging

def setup_logger(name, log_file, level=logging.INFO):
    """
    Set up a logger for the application.

    Args:
        name (str): The name of the logger.
        log_file (str): File path for the log file.
        level (int): Logging level.

    Returns:
        logging.Logger: Configured logger instance.

    Raises:
        IOError: If logger setup fails.
    """
    try:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger
    except Exception as e:
        raise IOError(f"Logger setup failed: {str(e)}")
