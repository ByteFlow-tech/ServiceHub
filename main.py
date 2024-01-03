import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from hub import Hub
from wss_connection_manager import WSConnectionManager

app: FastAPI = FastAPI()
ws_manager: WSConnectionManager = WSConnectionManager()
hub: Hub = Hub()


@app.websocket("/ws/service/{service_name}")
async def websocket_connection(websocket: WebSocket, service_name: str):
    try:
        await ws_manager.connect(websocket, service_name)
        while True:
            incoming: dict = await websocket.receive_json()
            handle_message = hub.incoming_message_handle(**incoming)
            # logic in developing
            pass
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
        # logic in developing


if __name__ == '__main__':
    uvicorn.run(app, port=23390)
