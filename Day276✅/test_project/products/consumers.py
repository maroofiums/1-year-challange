from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            "message": "Connected successfully"
        }))

    def receive(self, text_data):
        self.send(text_data=json.dumps({
            "message": text_data
        }))

    def disconnect(self, close_code):
        pass
