import time
import signal

import logging
logger = logging.getLogger(__name__)

class Looper():
    """
        Helper class for looping over functions, and listening to signals
        Not safe for multi-threading
    """
    def __init__(self):
        self.exit_requested = False

    def request_exit(self, _signum, _frame):
        """Handler for (graceful) exit requests."""
        print('** Exit requested. Please wait for the pending operation to complete. **')
        self.exit_requested = True

    def capture_signals(self):
        signal.signal(signal.SIGINT, self.request_exit)
        signal.signal(signal.SIGTERM, self.request_exit)

    def loop(self, interval, func, *args):
        """ Perform the looping of the func """

        logger.info('Looper process starting for function \'{0}\''.format(str(func.__name__)))
        while not self.exit_requested:
            func(*args)
            logger.debug("Sleeping for {0} seconds".format(interval))
            self.granular_sleep(interval)
        logger.info('Looper process ending for function \'{0}\''.format(str(func.__name__)))

    def granular_sleep(self, interval):
        """ Sleep, but in consideration of the signals in 1 sec intervals """
        for interval_part in range(0, interval):
            if not self.exit_requested:
                time.sleep(1) 