import asyncio
import websockets
from networktools.colorprint import gprint, bprint, rprint

import simplejson as json
"""
ws = create_connection(url)
print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
"""

class Websocket:
    def __init__(self, *args, **kwargs):
        self.ws_url=kwargs['ws_url']
        self.status=False

    async def connect(self):
        bprint("Generando conexión")
        try:
            ws = await websockets.connect(self.ws_url)
            self.status=True
            return ws
        except:
            self.status=False
            raise

    def connected(self):
        return self.status

    def url(self):
        return self.ws_url

    async def manage_data(self, ws, data):
        print(data)
        msg={'stream':'datashow','payload':data}
        bprint("El mensaje a enviar a backend:")
        gprint(msg)
        await ws.send(json.dumps(msg))

    def recv_acl(self,ws):
        print(ws.recv())

    async def close(self,ws):
        await ws.close()
