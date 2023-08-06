from watched_sdk import Addon
from .watched_local import watched_local

class KodiAddon(Addon):
    addAddonAsSource = False

    def get_cache(self):
        data = super(KodiAddon, self).get_cache(watched_local.sys.argv)
        if not data: return False
        watched_local.items = data['items']
        watched_local.item = data['item']
        watched_local.url = data['url']
        return True

    def set_cache(self):
        data = {
            'items': watched_local.items,
            'item': watched_local.item,
            'url': watched_local.url,
        }
        return super(KodiAddon, self).set_cache(watched_local.sys.argv, data)

    def delete_cache(self):
        super(KodiAddon, self).delete_cache(watched_local.sys.argv)

    # Kodi naming style

    def resetContext(self, resourceId, ctx, argv):
        watched_local.reset(self, resourceId, ctx, argv)

    def defaultDirectory(self):
        if not self.get_cache():
            self.onDirectory()
            self.set_cache()
        return {
            'items': watched_local.items,
            'hasMore': False
        }

    def defaultMetadataWithSeries(self, type, ids):
        if type == 'series':
            if not self.get_cache():
                self.onMetadataSeries()
                self.set_cache()
            return {
                'type': type,
                'ids': ids,
                'children': watched_local.items
            }
        else:
            if not self.get_cache():
                self.onMetadata()
                self.set_cache()
            return watched_local.item

    def defaultResolve(self):
        if not self.get_cache():
            self.onResolve()
            self.set_cache()
        return {'url': watched_local.url}

    def onDirectory(self):
        self.onRun()

    def onMetadataSeries(self):
        self.onRun()

    def onMetadata(self):
        self.onRun()

    def onResolve(self):
        self.onRun()

    def onRun(self):
        raise NotImplementedError()
