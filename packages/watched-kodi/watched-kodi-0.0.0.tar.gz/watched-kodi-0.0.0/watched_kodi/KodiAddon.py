from watched_sdk import WorkerAddon
from .watched_local import watched_local


class KodiAddon(WorkerAddon):
    """This will add the item ID as a item.sources object
    """
    add_addon_as_source = False

    def get_cache(self):
        data = super(KodiAddon, self).get_cache(watched_local.sys.argv)
        if not data:
            return False
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

    def reset_context(self, ctx, resourceId, argv):
        watched_local.reset(self, ctx, resourceId, argv)

    def default_directory(self):
        if not self.get_cache():
            self.kodi_directory()
            self.set_cache()
        return {
            'items': watched_local.items,
            'hasMore': False
        }

    def default_item(self, type, ids):
        if type == 'series':
            if not self.get_cache():
                self.kodi_itemSeries()
                self.set_cache()
            return {
                'type': type,
                'ids': ids,
                'children': watched_local.items
            }
        else:
            if not self.get_cache():
                self.kodi_item()
                self.set_cache()
            return watched_local.item

    def default_resolve(self):
        if not self.get_cache():
            self.kodi_resolve()
            self.set_cache()
        return {'url': watched_local.url}

    def kodi_directory(self):
        self.kodi_run()

    def kodi_itemSeries(self):
        self.kodi_run()

    def kodi_item(self):
        self.kodi_run()

    def kodi_resolve(self):
        self.kodi_run()

    def kodi_run(self):
        raise NotImplementedError()
