letslog
===============
This is a log module for people to log for their programs  
  
#### Required Packages
`datetime`, `logging`, `pathlib`

#### Available Levels 
INFO, DEBUG, WARNING, ERROR, CRITICAL

#### Constructor
`letslog.Letslog` constructor takes in 2 arguments with default option, one is `logPath` which states which folder that we want our log files to be put in, the other is `absolute` to indicate whether the first argument is an absolute path.  

The default value for `logPath` is `..\log` relative to the current working directory.  
The default value for `absolute` is True.  

*For example*:
If the current working directory is `~\Documents\my_program\src`, and we want to initiate a log file at an already created folder `~\Documents\my_program\log`  
The following code sample can achieve such goal:
```py
ll1 = letslog.Letslog()                                 # Uses default arguments
ll2 = letslog.Letslog('..\log', absolute=False)         # Uses relative path   
ll3 = letslog.Letslog('~\Documents\my_program\log')     # Uses absolute path  
```  

#### File Name
when we call `ll.initiateLogger('logger_id', 'INFO')`, we create a log with name `<current datetime>+<logger_id>.log`

#### Usage
```py
import letslog

ll = letslog.Letslog()                                  # Sets the log file location to default location
ll.initiateLogger('logger_id', 'INFO')                  # The created log file will be at '~\Documents\my_program\log\2020-06-24_203352logger_id.log'
ll.setLevel('WARNING')                                  # We could change the level of this logger
ll.log('This is a warning!')                            # We could write a message to the logger using current logger level
```
