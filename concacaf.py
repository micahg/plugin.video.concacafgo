# actually websocket-client in pip
from websocket import create_connection
from json import loads

def get_streams():
    """Get the streams"""
    ws = create_connection('wss://s-usc1b-nss-2164.firebaseio.com/.ws?v=5&ns=goldcup2017-prod')
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
