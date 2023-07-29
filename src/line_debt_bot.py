from debt_manager import DebtManager
from message import Message

class LineBotHandler:
    def __init__(self, table_name):
        self.debt_manager = DebtManager(table_name)

    def handle_message(self, event):
        # ユーザからのメッセージイベントを処理し、適切な応答を生成します。
        for message in event['events']:
            if message['type'] == 'message' and message['message']['type'] == 'text':
                # Messageクラスのインスタンスを作成します。
                msg = Message(message['message']['type'], message['message']['text'], message['source'])
                self.handle_text_message(msg)

    def handle_text_message(self, message):
        """_summary_

        Args:
            message (_type_): "A -> B 1000" 
        """
        message_text = message['message']['text']
        message_list = message_text.replace("->", "").split()
        user_id1, user_id2, amount = message_list[0], message_list[1], int(message_list[2])
        self.debt_manager.add_debt(user_id1, user_id2, amount)