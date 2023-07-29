import json
import urllib.request
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Transactions')

def lambda_handler(event, context):
    print(event)
    messages = json.loads(event['body'])['events']
    for message in messages:
        text = message['message']['text']
        sender = message['source']['userId']
        reply_token = message['replyToken']

        if '->' not in text or len(text.split(' ')) != 4:
            reply_text = 'メッセージのフォーマットが正しくありません。正しいフォーマットは「貸主 -> 借主 金額」です。'
        else:
            parts = text.split(' ')
            amount = parts[3]

            if amount.endswith('円'):
                amount = int(amount[:-1])
            lender, borrower = parts[0], parts[2]

            # DynamoDBへの保存
            table.put_item(
                Item={
                    'lender': lender,
                    'borrower': borrower,
                    'amount': amount,
                }
            )
            reply_text = f'{lender}が{amount}円を{borrower}に貸しました。'

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

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'ok',
        }),
    }
