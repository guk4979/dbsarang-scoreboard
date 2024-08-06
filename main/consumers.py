from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ScoreConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 그룹에 가입합니다
        await self.channel_layer.group_add(
            'score_update',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # 그룹에서 탈퇴합니다
        await self.channel_layer.group_discard(
            'score_update',
            self.channel_name
        )

    async def send_message(self, event):
        # 클라이언트에 메시지를 보냅니다
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))