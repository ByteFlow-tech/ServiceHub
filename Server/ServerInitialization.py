import asyncio
import websockets


async def handler(websocket):
    while True:
        print(f"Connection established by {websocket}")
        try:
            message = await websocket.recv()
            print("Message received: " + message)
            await websocket.send("server state up")
        except Exception as e:
            print(e)
            break


async def websocket_server_initialization():
    await asyncio.sleep(1)
    print("Server starting...")
    async with websockets.serve(handler, "localhost", 7777):
        await asyncio.sleep(1)
        print("Server is running")
        await asyncio.Future()
