from .watched_local import watched_local

class Addon:
    def __init__(self, id=None):
        self.id = id or watched_local.addon.id
        self.settings = {}

    def getAddonInfo(self, key):
        return key

    def getLocalizedString(self, str):
        return str

    def getSetting(self, key):
        self.settings.get(key)

    def setSetting(self, key, value):
        self.settings[key] = value
