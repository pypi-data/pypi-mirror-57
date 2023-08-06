class StreamToLogger(object):
    def __init__(self, logger):
        self.logger = logger

    def write(self, message):
        for line in message.rstrip().splitlines():
            self.logger.info(line.rstrip())

    def flush(self):
        pass
