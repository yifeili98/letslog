import logging, datetime, os, pathlib

class Letslog:
    def __init__(self, logPath=(pathlib.Path().absolute().parent/'log').as_posix(), absolute=True):
        '''Initiate Letslog object with specified log folder.

        Args:
            logPath: The absolute path to the log folder
        Raises:
            KeyError: The level parameter is not valid
        Returns:
            None
        '''
        self.logger = None
        if absolute:
            self.logPath = logPath
        else:
            self.logPath = (pathlib.Path().absolute() / logPath).as_posix()
        try:
            assert os.path.isdir(self.logPath)
        except:
            raise OSError('No such directory: ' + self.logPath)

    def initiateLogger(self, origin, level):
        '''Initiate a logger with given logging level and logging origin.

        Args:
            origin: From which source this logger is from (for determining logging file name)
            level: The level of the logger, options are [INFO, DEBUG, WARNING, ERROR, CRITICAL]
        Raises:
            KeyError: The level parameter is not valid
        Returns:
            None
        '''
        try:
            print(self.logPath)
            logging.basicConfig(filename = self.logPath + '/' +
                    str(datetime.datetime.now()).replace(' ', '_').replace(':', '')[:17] + origin + '.log', 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            self.logger = logging.getLogger(__name__)
            self.setLevel(level)
        except:
            raise KeyError("Invalid logger level")

    def getNativeLogger(self):
        '''Get the native logging module logger.

        Returns:
            The logger object
        '''
        return self.logger

    def getLevel(self):
        '''Get the current level of this logger as a string.

        Returns:
            The logger level
        '''
        try:
            self._checkLogger()
            pass
        except:
            return -1
        else:
            val = self.logger.level
            if val == 10:
                return 'DEBUG'
            elif val == 20:
                return 'INFO'
            elif val == 30:
                return 'WARNING'
            elif val == 40:
                return 'ERROR'
            elif val == 50:
                return 'CRITICAL'
            else:
                return 'NONSET'

    def setLevel(self, level):
        '''Set the level of the logger.

        Args:
            level: The level of the logger, options are [INFO, DEBUG, WARNING, ERROR, CRITICAL]
        Raises:
            KeyError: The level parameter is not valid
            ValueError: The logger has not initiated
        Returns:
            None
        '''
        try:
            self._checkLogger()
            self.logger.setLevel(level)
        except ValueError as ve:
            raise ve
        except:
            raise KeyError("Invalid logger level!")

    def log(self, message):
        '''Write a message to the log using the logger level.

        Args:
            message: The message that is going to be written to log
        Raises:
            ValueError: The logger is not initiated
            ValueError: The logger level was initiated incorrectly
        Returns:
            None
        '''
        try:
            self._checkLogger()
            if self.logger.level == -1:
                raise ValueError('The logger level was initiated incorrectly!')
            self.logger.log(self.logger.level, message)
        except Exception as e:
            raise e

    def _checkLogger(self):
        '''Check if logger is initiated.

        Args:
            None
        Raises:
            ValueError: The logger is not initiated
        Returns:
            None
        '''
        if not self.logger:
            raise ValueError('The logger is not initiated!')


