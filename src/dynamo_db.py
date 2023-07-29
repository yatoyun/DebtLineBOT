import boto3

class DynamoDB:
    def __init__(self, table_name):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table(table_name)
        
    def get_item(self, key):
        # get item from DynamoDB using the key
        response = self.table.get_item(Key=key)
        return response

    def put_item(self, item):
        # put item into DynamoDB
        response = self.table.put_item(Item=item)
        return response

    def update_item(self, key, update_expression, expression_attribute_values):
        response = self.table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues='UPDATED_NEW'
        )
        return response