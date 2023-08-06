import sys
import logging.handlers


class AnalyticsHandler(logging.handlers.MemoryHandler):

    def __init__(self, client=None, *args, **kwargs):
        self.client = client
        self.stream = sys.stderr
        super().__init__(*args, **kwargs)

    def flush(self):
        for record in self.buffer:
            self.emit(record)

    def emit(self, record):
        """
        Override to post to logger
        """
        try:
            msg = self.format(record)
            stream = self.stream
            # issue 35046: merged two stream.writes into one.
            stream.write('AnalyticsHandler: ' + msg + '\n')
            self.flush()
        except Exception:
            self.handleError(record)
