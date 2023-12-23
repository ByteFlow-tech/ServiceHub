import asyncio
import websockets

from Core.Exceptions import Stop


async def handler(websocket):
    print("Waiting connections...")
    while True:
        print(f"Connection established by {websocket}")
        try:
            message = await websocket.recv()
            print("Message received: " + message)
            await websocket.send("server state up")
        except Exception as e:
            print(e)
            break


async def websocket_server_initialization(port):
    await asyncio.sleep(1)
    port = 7777 if port is None else port
    print(f"Server starting on port {port}...")

    async with websockets.serve(handler, "localhost", port):
        print("Server is running")


