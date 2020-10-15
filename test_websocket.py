import asyncio
import websockets
from datetime import datetime


async def start_connection():
    async with websockets.connect("ws://echo.websocket.org") as myWebSocket:
        await myWebSocket.send("so, verbindung steht")
        print(await myWebSocket.recv())
        await asyncio.gather(
            msg_sender(myWebSocket),
            msg_recv(myWebSocket),
            stop_connection(myWebSocket)
            )

        return myWebSocket

async def stop_connection(ws):
    await asyncio.sleep(6)
    await ws.close()

async def msg_recv(ws):
    while ws:
        async for incoming_msg in ws:
            print(incoming_msg)
            
            
async def msg_sender(ws):
    while ws:
        dt = datetime.now()
        await ws.send("die aktuelle Uhrzeit ist: " + dt.strftime("%H:%M:%S"))
        await asyncio.sleep(2)

async def ws_client():
    open_websocket = await start_connection()
    await open_websocket.send("hi, my name is...")
    async for incoming_msg in open_websocket:
        print(incoming_msg)

#Sync part
asyncio.get_event_loop().run_until_complete(ws_client())