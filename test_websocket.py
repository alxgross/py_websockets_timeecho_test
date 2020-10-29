import asyncio
import websockets
from datetime import datetime
import sys


class myWebsocket:

    async def connect(self):
        self.websocket = await websockets.client.connect("ws://echo.websocket.org")

        await self.websocket.send("so, verbindung steht")
        print(await self.websocket.recv())
#             await asyncio.gather(
#                 msg_sender(myWebSocket),
#                 msg_recv(myWebSocket),
#     #            user_msg(myWebSocket),
#                 stop_connection(myWebSocket)
#                 )

           # return myWebSocket

    async def stop_connection(ws):
        await asyncio.sleep(6)
        await ws.close()

    async def start_receiver(self):
        while self.websocket:
            incoming_msg = await self.websocket.recv()
            print("Message from Server: ", incoming_msg)
                
                
    async def send(self, message):
        while self.websocket:
            dt = datetime.now()
            await self.websocket.send(message + "und die aktuelle Uhrzeit ist: " + dt.strftime("%H:%M:%S"))
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

    async def consumer_handler(self) -> None:
        async for message in self.websocket:
            print(message)
            
    async def consume(self):
        await self.connect()

    def __init__(self):
        pass


# Sync part
if __name__ == '__main__':
    
    myWs = myWebsocket()
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(myWs.connect())

    # Start listener and heartbeat 
    tasks = [
        asyncio.ensure_future(myWs.send("irgendwas...")),
        asyncio.ensure_future(myWs.start_receiver()),
    ]

    loop.run_until_complete(asyncio.wait(tasks))

