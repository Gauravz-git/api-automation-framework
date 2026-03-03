import logging
import os

def get_logger():
    logger = logging.getLogger("APIAutomation")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        os.makedirs("reports", exist_ok=True)
        handler = logging.FileHandler("reports/api.log")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger