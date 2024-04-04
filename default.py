import xbmcplugin
import xbmcgui

import routing

from json import loads
from websocket import create_connection

plugin = routing.Plugin()

def get_streams():
    """Get the streams"""
    ws = create_connection('wss://s-usc1b-nss-2166.firebaseio.com/.ws?v=5&ns=goldcup2017-prod')
    ws.recv()
    ws.send('{"t":"d","d":{"r":1,"a":"s","b":{"c":{"sdk.js.7-7-0":1}}}}')
    ws.recv()
    ws.send('{"t":"d","d":{"r":2,"a":"q","b":{"p":"/data_v1_3/editions/appSettings/general/videoStreams","h":""}}}')
    num = ws.recv()
    json_buf = ''
    for _ in range(int(num)):
        json_buf += ws.recv()
    ws.close()
    js_obj = loads(json_buf)
    return js_obj['d']['b']['d']

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
