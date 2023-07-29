from src.dynamo_db import DynamoDB
# DebtManagerクラスを作成します。各メソッド内にエラーハンドリングを追加します。

class DebtManager:
    def __init__(self, table_name):
        self.dynamo_db = DynamoDB(table_name)

    def get_debt(self, user_id1, user_id2):
        # user_id1からuser_id2への借金の量を取得します。
        try:
            key = {
                'user_id1': user_id1,
                'user_id2': user_id2
            }
            response = self.dynamo_db.get_item(key)
            return response["item"].get("debt")
        except Exception as e:
            print(f"Error getting debt: {str(e)}")
            return None

    def set_debt(self, user_id1, user_id2, amount):
        # user_id1からuser_id2への借金の量を設定します。
        try:
            item = {
                'user_id1': user_id1,
                'user_id2': user_id2,
                'debt': amount
            }
            response = self.dynamo_db.put_item(item)
        except Exception as e:
            return (f"Error setting debt: {str(e)}")

    def add_debt(self, user_id1, user_id2, amount):
        # user_id1からuser_id2への借金の量を増やします。
        try:
            key = {
                'user_id1': user_id1,
                'user_id2': user_id2
            }
            update_expression = 'ADD amount :inc'
            expression_attribute_values = {':inc': int(amount)}
            return_values='UPDATED_NEW'
            response = self.dynamo_db.update_item(key, update_expression, expression_attribute_values, return_values)
        except Exception as e:
            return (f"Error adding debt: {str(e)}")
