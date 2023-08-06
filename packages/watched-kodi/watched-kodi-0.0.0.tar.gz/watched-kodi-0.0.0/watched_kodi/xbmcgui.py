from .common import logger

class ListItem:
    def __init__(self, name=None, **infos):
        self.infos = infos
        self.infos['name'] = name
        self.arts = {}
        self.stream = {}
        self.props = {}
        self.subtitles = []
        logger.debug('ListItem.__init__ %s %s', name, infos)

    def setPath(self, path):
        logger.debug('ListItem.setPath %s', path)
        self.infos['path'] = path

    def setInfo(self, key=None, value=None, **kwargs):
        logger.debug('ListItem.setInfo %s=%s %s', key, value, kwargs)
        if key:
            self.infos[key] = value
        self.infos.update(kwargs)

    def setArt(self, args):
        logger.debug('ListItem.setArt %s', args)
        self.arts.update(args)

    def addStreamInfo(self, key, value):
        logger.debug('ListItem.addStreamInfo %s %s', key, value)
        self.stream[key] = value

    def addContextMenuItems(self, menu, replaceItems=None):
        logger.debug('ListItem.addContextMenuItems %s, replaceItems=%s', menu, replaceItems)
        pass

    def setProperty(self, key, value):
        logger.debug('ListItem.setProperty %s %s', key, value)
        self.props[key] = value

    def setSubtitles(self, subtitles):
        logger.debug('ListItem.setSubtitles %s', subtitles)
        self.subtitles = subtitles

class Dialog:
    def __init__(self):
        pass

    def ok(self, title, msg):
        logger.debug('Dialog: [%s] %s', title, msg)
