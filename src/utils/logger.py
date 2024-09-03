import logging

LOGGING_LEVEL = logging.INFO


class CustomFormatter(logging.Formatter):
    """Custom formatter to add color to log levels and create clickable links."""

    def format(self, record):
        levelname = record.levelname
        if levelname == "DEBUG":
            record.levelname_color = "\033[94mDEBUG\033[0m"
        elif levelname == "INFO":
            record.levelname_color = "\033[92mINFO\033[0m"
        elif levelname == "WARNING":
            record.levelname_color = "\033[93mWARNING\033[0m"
        elif levelname == "ERROR":
            record.levelname_color = "\033[91mERROR\033[0m"
        elif levelname == "CRITICAL":
            record.levelname_color = "\033[95mCRITICAL\033[0m"
        else:
            record.levelname_color = levelname

        record.pathname_lineno = f"\033]8;;file://{record.pathname}:{record.lineno}\033\\{record.filename}:{record.lineno}\033]8;;\033\\"

        return super().format(record)


def configure_logger() -> None:
    """Configure the global logger with a custom format."""
    formatter = CustomFormatter("%(levelname_color)s\t%(pathname_lineno)s\t%(message)s")

    ch = logging.StreamHandler()
    ch.setLevel(LOGGING_LEVEL)
    ch.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(LOGGING_LEVEL)
    logger.addHandler(ch)


configure_logger()
