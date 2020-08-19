import logging
import logging.config


class AppLogger:
    def __init__(self, name):
        logging.config.fileConfig('app/logger.conf')
        self.logger = logging.getLogger(name)

