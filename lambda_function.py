from .src.line_debt_bot import LineBotHandler
from .src.message import Message

def lambda_handler(event, context):
    # Lineからのメッセージをパースする
    messages = parse_line_messages(event)
    
    # LineBotHandlerを初期化する
    bot_handler = LineBotHandler(table_name="DebtLineBot")
    
    # 各メッセージを処理する
    for message in messages:
        bot_handler.handle_message(message)

def parse_line_messages(event):
    messages = []
    for msg in event:
        message = Message(msg['type'], msg['text'], msg['source'])
        messages.append(message)
    return messages
