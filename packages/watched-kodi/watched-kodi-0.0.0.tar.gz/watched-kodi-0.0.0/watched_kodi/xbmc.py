from .common import logger

LOGDEBUG = 0
LOGNOTICE = 1
LOGWARNING = 2
LOGERROR = 3

LEVELS = {
    LOGDEBUG: logger.debug,
    LOGNOTICE: logger.info,
    LOGWARNING: logger.warning,
    LOGERROR: logger.error,
}

def executebuiltin(str):
    return ''

def translatePath(path):
    return ''

def getInfoLabel(label):
    return label

def executeJSONRPC(*args, **kwargs):
    return ''

def log(msg, level=LOGDEBUG):
    LEVELS.get(level, logger.critical)(msg)
