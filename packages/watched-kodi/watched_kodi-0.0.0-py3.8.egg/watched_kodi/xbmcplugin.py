from .watched_local import watched_local
from .common import logger

SORT_METHOD_UNSORTED = 'unsorted'
SORT_METHOD_TITLE = 'title'
SORT_METHOD_EPISODE = 'episode'

_CONVERT_CONTENT = {
    'files': 'directory',
    'movie': 'movie',
    'movies': 'movie',
    'tvshow': 'series',
    'tvshows': 'series',
    'episode': 'episode',
    'episodes': 'episode',
}

_VIDEO_KEYS = {
    'name': 'name',
    'Title': 'name',
    'Plot': 'description',
    'Year': 'year',
    'Duration': 'duration',
}
_INFO_LABELS_KEYS = {
    'year': 'year',
    'cast': 'cast',
    'title': 'name',
    'plot': 'description',
}
_ARTS_KEYS = {
    'fanart': 'backdrop',
    'thumb': 'poster',
}

def convertListItem(liz, playable=False):
    path = liz.infos['path']
    item = {
        'type': _CONVERT_CONTENT.get(watched_local.content, watched_local.content) or 'directory',
        'name': liz.infos.pop('name') or liz.infos.pop('label'),
        'images': {}
    }

    # ids
    if item['type'] == 'directory':
        item['id'] = path
        item['args'] = {'resourceId': watched_local.resourceId}
    else:
        item['ids'] = {watched_local.addon.id: path}

    # infos
    #if 'type' in liz.infos:
    #    item['type'] = _CONVERT_CONTENT[liz.infos.pop('type')]
    if liz.infos.get('thumbnailImage'):
        item['images']['poster'] = liz.infos.pop('thumbnailImage')

    # infos.Video
    video = liz.infos.get('Video', {})
    if 'mediatype' in video:
        item['type'] = _CONVERT_CONTENT[video.pop('mediatype')]
    for key, alias in _VIDEO_KEYS.items():
        if key in video:
            item[alias] = video.pop(key)

    # infos.infoLabels
    infoLabels = liz.infos.get('infoLabels', {})
    for key, alias in _INFO_LABELS_KEYS.items():
        if key in infoLabels:
            item[alias] = infoLabels.pop(key)
    if 'code' in infoLabels:
        item['ids']['imdb_id'] = infoLabels.pop('code')
    if 'director' in infoLabels:
        item['director'] = [infoLabels.pop('director')]

    # arts
    for key, alias in _ARTS_KEYS.items():
        if key in liz.arts:
            img = liz.arts.pop(key)
            if img:
                item['images'][alias] = img

    # source
    if (playable or item['type'] != 'directory') and watched_local.addon.addAddonAsSource:
        if 'sources' not in item:
            item['sources'] = []
        item['sources'].append({
            'id': path,
            'url': 'watched-addon:'+watched_local.addon.id+'/'+path
        })

    # finalize
    if item['type'] == 'episode':
        del item['type']
        item['season'] = video['Season']
        item['episode'] = video['Episode']

    # print(item)
    # print(liz)
    # print(liz.infos)
    # print("---")
    # print(infoLabels)
    # print("---")
    # print(info)
    # print("---")
    # raise XXX
    return item

def setContent(ignoredId, content):
    logger.debug('setContent %s', content)
    watched_local.content = content

def addSortMethod(ignoredId, method):
    logger.debug('addSortMethod %s', method)
    watched_local.sort.append(method)

def addDirectoryItems(ignoredId, items, length):
    logger.debug('addDirectoryItems %s', items)
    for url, liz, playable in items:
        watched_local.tempItems.append((url, liz, playable))

def addDirectoryItem(handle=None, url=None, listitem=None, isFolder=False, totalItems=0):
    logger.debug('addDirectoryItem %s', (url, listitem, not isFolder))
    watched_local.tempItems.append((url, listitem, not isFolder))

def endOfDirectory(ignoredId=None, cacheToDisc=False, succeeded=True):
    logger.debug('endOfDirectory %s', cacheToDisc)
    for path, liz, playable in watched_local.tempItems:
        if path and not liz.infos.get('path'):
            liz.infos['path'] = path
        watched_local.items.append(convertListItem(liz, playable))
        # if liz.infos:
        #     print('infos', liz.infos)
        # if liz.arts:
        #     print('arts', liz.arts)
        # if liz.stream:
        #     print('stream', liz.stream)
        # if liz.props:
        #     print('props', liz.props)
        # if liz.subtitles:
        #     print('subtitles', liz.subtitles)

    watched_local.end.set()

def setResolvedUrl(ignoredId, succeeded, listitem):
    logger.debug('setResolvedUrl %s %s', succeeded, listitem)
    watched_local.succeeded = succeeded
    watched_local.resolved = listitem
    watched_local.url = listitem.infos['path']
    watched_local.end.set()
