from assertpy import assert_that
from api_client.base import APIClient

class LoginAPI(APIClient):
    def __init__(self):
        super().__init__()
        self.base_url = "https://spot-api.moco.co.id/backend/auth/login"

    def post_login(self,login_email,login_password):
        payload = {
            "email":login_email,
            "password":login_password
        }
        return self.post(self.base_url,json = payload)

    def post_token(self,txtemail,txtpassword,txttoken,txtorganization_id,txtuser_id):
        payload = {
            "email":txtemail,
            "password":txtpassword,
            "token":txttoken,
            "organization_id":txtorganization_id,
            "user_id":txtuser_id
        }
        return self.post(self.base_url,json=payload)



