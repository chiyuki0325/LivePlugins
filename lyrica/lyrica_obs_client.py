import asyncio
import websockets
import json


async def listen():
    uri = "ws://127.0.0.1:15649/ws"
    metadata = ""
    async with websockets.connect(uri) as websocket:
        while True:
            message = json.loads(await websocket.recv())
            match message["id"]:
                case 0:
                    metadata = "当前正在播放: " + message["data"]["music_info"]["artist"] + " - " + message["data"]["music_info"]["title"] + "\n"
                case 1:
                    with open("/tmp/lyric_line.txt", "w") as file:
                        file.write(metadata + message["data"]["lyric_line"]["lyric"])

asyncio.get_event_loop().run_until_complete(listen())
