import asyncio
import websockets
from datetime import datetime
import sys


async def start_connection():
    async with websockets.connect("ws://echo.websocket.org") as myWebSocket:
        await myWebSocket.send("so, verbindung steht")
        print(await myWebSocket.recv())
        await asyncio.gather(
            msg_sender(myWebSocket),
            msg_recv(myWebSocket),
#            user_msg(myWebSocket),
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
        
async def user_msg():
#    while ws:
#        await asyncio.sleep(1)
#        user_input = await input("Write something: ")
#        await ws.send("Filler_message")
    print("blblbl")

async def ws_client():
    open_websocket = await start_connection()
    await open_websocket.send("hi, my name is...")
    async for incoming_msg in open_websocket:
        print(incoming_msg)


#Sync part
q = asyncio.Queue()
#fut = asyncio.ensure_future(q.get())
#fut.add_done_callback(user_msg)
loop = asyncio.get_event_loop()
#loop.add_reader(sys.stdin, got_stdin_data, q)
loop.run_until_complete(ws_client())

