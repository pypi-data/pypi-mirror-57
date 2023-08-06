import sys
from . import xbmc
from . import xbmcaddon
from . import xbmcgui
from . import xbmcplugin
from . import xbmcvfs
from .watched_local import watched_local
from .KodiAddon import KodiAddon

sys.modules['xbmc'] = xbmc
sys.modules['xbmcaddon'] = xbmcaddon
sys.modules['xbmcgui'] = xbmcgui
sys.modules['xbmcplugin'] = xbmcplugin
sys.modules['xbmcvfs'] = xbmcvfs
sys.modules['watched_local'] = watched_local
