from src.dynamo_db import DynamoDB

class DebtManager:
    def __init__(self):
        self.dynamo_db = DynamoDB()

    def get_debt(self, user_id1, user_id2):
        # user_id1からuser_id2への借金の量を取得します。
        pass

    def set_debt(self, user_id1, user_id2, amount):
        # user_id1からuser_id2への借金の量を設定します。
        pass

    def add_debt(self, user_id1, user_id2, amount):
        # user_id1からuser_id2への借金の量を増やします。
        pass

    def reduce_debt(self, user_id1, user_id2, amount):
        # user_id1からuser_id2への借金の量を減らします。
        pass