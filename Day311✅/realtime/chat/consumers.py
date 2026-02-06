from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            "message": "You are connected!"
        }))
    
    async def disconnect(self, close_code):
        print("WebSocket disconnected with code:", close_code)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '')

        await self.send(text_data=json.dumps({
            "message": f"You said: {message}"
        }))
        