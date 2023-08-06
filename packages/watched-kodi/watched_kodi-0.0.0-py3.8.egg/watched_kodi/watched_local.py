import threading

class Sys(threading.local):
    def __init__(self):
        self.argv = None

class Local(threading.local):
    def __init__(self):
        self.sys = Sys()
        self.reset()

    def reset(self, addon=None, resourceId=None, ctx=None, argv=None):
        self.addon = addon
        self.resourceId = resourceId
        self.ctx = ctx
        self.sys.argv = argv

        # Output variables
        self.content = ''
        self.sort = []
        self.tempItems = []
        self.items = []
        self.item = None
        self.url = None
        self.end = threading.Event()

watched_local = Local()
