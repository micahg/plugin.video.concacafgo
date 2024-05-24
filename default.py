import xbmcplugin
import xbmcgui

import routing

from concacaf import get_streams


plugin = routing.Plugin()


@plugin.route('/')
def main_menu():
    """Populate the menu with the main menu items."""
    handle = plugin.handle
    xbmcplugin.setContent(handle, 'videos')
    all_streams = get_streams()
    for k in all_streams:
        strm = all_streams[k]
        title = strm['title']
        status = strm['status']
        image = strm['img']
        url = strm['uri']
        item = xbmcgui.ListItem(f'{status} - {title}')
        item.setArt({'thumb': image, 'poster': image})
        xbmcplugin.addDirectoryItem(handle, url, item)
    xbmcplugin.endOfDirectory(handle)

if __name__ == '__main__':
    plugin.run()
