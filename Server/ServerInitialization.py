import ast
#
import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from starlette.websockets import WebSocketState

from Server.Hub.Hub import Hub

app = FastAPI()
hub = Hub()
sessions = []


@app.websocket('/ws/')
async def service_connector(websocket: WebSocket):
    await websocket.accept()
    origin_service, origin_port = websocket.client
    state = "OK" if websocket.client_state == WebSocketState.CONNECTED else "BAD"
    session_id = hub.add_connection(origin_service, origin_port, state)
    sessions.append({"id": session_id, "session": websocket})
    try:
        while True:
            data = await websocket.receive_text()
            data = ast.literal_eval(data)
            session_id = hub.get_target_session(data['headers']["target-unique-service-name"])
            for session in sessions:
                if session["id"] == session_id[0]:
                    await session["session"].send_text(str(data))
    except WebSocketDisconnect:
        hub.del_connection(origin_service)


@app.get('/state')
async def get_state():
    return "OK"

if __name__ == '__main__':
    uvicorn.run(app, port=7777)
