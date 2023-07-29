from src.dynamo_db import DynamoDB

class DebtManager:
    def __init__(self, table_name):
        self.dynamo_db = DynamoDB(table_name)

    def get_debt(self, user_id1, user_id2):
        # user_id1からuser_id2への借金の量を取得します。
        key = {
            'user_id1': user_id1,
            'user_id2': user_id2
        }
        item = self.dynamo_db.get_item(key)
        return item.get('debt', 0)

    def set_debt(self, user_id1, user_id2, amount):
        # user_id1からuser_id2への借金の量を設定します。
        item = {
            'user_id1': user_id1,
            'user_id2': user_id2,
            'debt': amount
        }
        self.dynamo_db.put_item(item)

    def add_debt(self, user_id1, user_id2, amount):
        # user_id1からuser_id2への借金の量を増やします。
        current_debt = self.get_debt(user_id1, user_id2)
        new_debt = current_debt + amount
        self.set_debt(user_id1, user_id2, new_debt)

    def reduce_debt(self, user_id1, user_id2, amount):
        # user_id1からuser_id2への借金の量を減らします。
        current_debt = self.get_debt(user_id1, user_id2)
        new_debt = current_debt - amount
        self.set_debt(user_id1, user_id2, new_debt)