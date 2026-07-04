import logging

def get_logger(name: str = "ai_summer_lab", log_level: str = "logging.INFO") -> logging.Logger:
    logger = logging.getLogger(name)

    level = getattr(logging, log_level.upper(), logging.INFO)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger