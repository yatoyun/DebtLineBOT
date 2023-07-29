from debt_manager import DebtManager

class Message:
    def __init__(self, type, text, source):
        self.type = type
        self.text = text
        self.source = source


class LineBotHandler:
    def __init__(self):
        self.debt_manager = DebtManager()

    def handle_message(self, message):
        # ユーザからのメッセージを処理し、適切な応答を生成します。
        pass

    def handle_text_message(self, message):
        # ユーザからのテキストメッセージを処理します。
        pass