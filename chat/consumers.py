from channels.generic.websocket import AsyncWebsocketConsumer
import json
class ChatRoomConsumer(AsyncWebsocketConsumer):
    pass
    # async def connect(self):
    #     self.room_name = self.scope['url_route']['kwargs']['room_name']
    #     self.room_group_name = f'chat_{self.room_name}'
    #     await(self.channel_layer.group_add)(
    #         self.room_group_name,self.channel_name
    #     )
    #     self.accept()
    #     await(self.channel_layer.group_send)(
    #         self.room_group_name,
    #         {
    #             'type':'tester_message',
    #             'tester':'hello world'
    #         }
    #     )

        

    # async def tester_message(self,event):
    #     print(event)
    #     await self.send(text_data=json.dumps({
    #         'message':'succesful'
    #     }))
    # async def disconnect(self,close_code):
    #     await self.channel_layer.group_discard(
    #         self.room_group_name,
    #         self.channel_name
    #     )