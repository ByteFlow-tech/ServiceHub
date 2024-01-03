from fastapi import WebSocket


class WSConnectionManager:
    def __init__(self):
        self.active_connections: list[dict] = []

    async def connect(self, websocket: WebSocket, service_name: str):
        await websocket.accept()
        self.active_connections.append({"service-name": service_name,
                                        "connection": websocket})

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: WebSocket, target_service: str):
        for connection in self.active_connections:
            if connection["service-name"] == target_service:
                await connection["connection"].send_json(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection["connection"].send_json(message)