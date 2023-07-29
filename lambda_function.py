from src.line_debt_bot import LineBotHandler
from src.message import Message
import json


def lambda_handler(event, context):
    # LineBotHandlerを初期化する
    bot_handler = LineBotHandler(table_name="DebtLineBot")

    # Lineからのメッセージをパースする
    parse_line_messages(event, bot_handler)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "ok",
            }
        ),
    }


def parse_line_messages(event, bot_handler):
    for msg in json.loads(event["body"])["events"]:
        if msg["type"] == "message" and msg["message"]["type"] == "text":
            message = Message(msg["type"], msg["message"]["text"], msg["source"]["userId"])
            bot_handler.handle_message(message, msg["replyToken"])
        else:
            print("message type is not text")


