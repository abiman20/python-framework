import pytest
from Business_Functions.api.user import User

class Test_User:

    def test_post_user(self):
        create_user = User()
        create_user.post_user()
        create_user.verify_post_user()
        

    def test_get_user_by_id(self):
        self.user_id = 2
        user = User()
        user.get_user_by_id(self.user_id)
        user.verify_get_user_by_id(self.user_id)

    
