from src.debt_manager import DebtManager
from src.message import Message
import urllib.request
import os
import json


class LineBotHandler:
    def __init__(self, table_name):
        self.debt_manager = DebtManager(table_name)

    def handle_message(self, message, reply_token):
        """_summary_

        Args:
            message (_type_): "A -> B 1000", or "A - B", "A <- B 1000"
        """
        message_text = message.text
        
        if "->" in message.text:
            message_list = message_text.replace("->", "").split()
            user_id1, user_id2, amount = message_list[0], message_list[1], int(message_list[2])
            self.debt_manager.add_debt(user_id1, user_id2, amount)
            self.debt_manager.add_debt(user_id2, user_id1, -amount)
            reply_text = f"{user_id1}が{user_id2}に{amount}円を貸しました。"
        
        elif "<-" in message.text:
            message_list = message_text.replace("<-", "").split()
            user_id1, user_id2, amount = message_list[1], message_list[0], int(message_list[2])
            self.debt_manager.add_debt(user_id1, user_id2, amount)
            self.debt_manager.add_debt(user_id2, user_id1, -amount)
            reply_text = f"{user_id1}が{user_id2}に{amount}円を貸しました。"
        
        elif "-" in message.text:
            message_list = message_text.replace("-", "").split()
            assert len(message_list) == 2
            user_id1, user_id2, amount = message_list[0], message_list[1], 0
            self.debt_manager.set_debt(user_id1, user_id2, amount)
            self.debt_manager.set_debt(user_id2, user_id1, amount)
            reply_text = f"{user_id1}と{user_id2}の借金をinitしました。"
        
        elif "show" in message.text:
            message_list = message_text.replace("show", "").split()
            user_id1, user_id2 = message_list[0], message_list[1]
            amount = self.debt_manager.get_debt(user_id1, user_id2)
            reply_text = f"{user_id1}が{user_id2}に{amount}円貸りています。"
        
        
        # ユーザーにメッセージを返す
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + os.environ['ACCESS_TOKEN'],
        }
        data = {
            'replyToken': reply_token,
            'messages': [
                {
                    'type': 'text',
                    'text': reply_text,
                },
            ],
        }
        request = urllib.request.Request('https://api.line.me/v2/bot/message/reply', headers=headers, data=json.dumps(data).encode('utf-8'))
        urllib.request.urlopen(request)
