from pprint import pprint

import pytest
from assertpy import assert_that

from api_client.login import LoginAPI
from setting import Login

login = Login

@pytest.fixture
def login_api():
    return LoginAPI()

def test_login_positif(login_api):
    response = login_api.post_login(login_email=login.txtEmail,login_password=login.txtPassword)
    # data = response.json().get("payload")

    assert_that(response.status_code).is_equal_to(200)

    pprint(response.status_code)


data = login.list_login_negatif
input_result =[
    (f'{data['data1']['email']}',f'{data['data1']['password']}',f'{data['data1']['pesan']}'),
    (f'{data['data2']['email']}',f'{data['data2']['password']}',f'{data['data2']['pesan']}'),
    (f'{data['data3']['email']}',f'{data['data3']['password']}',f'{data['data3']['pesan']}')
]

@pytest.mark.parametrize('email,password,pesan',input_result)
def test_login_negatif(login_api,email,password,pesan):
    """
    skenario negatif tes login:
    email       password    pesan
    benar       salah       Password tidak sesuai.
    salah       benar       Pengguna tidak ditemukan.
    salah       salah       Pengguna tidak ditemukan.
    """
    response = login_api.post_login(login_email= f'{email}',login_password=f'{password}')

    assert_that(response.status_code).is_equal_to(401)

def test_token(login_api):
    response = login_api.post_token(txtemail=f'{login.txtEmail}',txtpassword=f'{login.txtPassword}',txttoken=f'{login.token}',txtorganization_id=f'{login.organization_id}',txtuser_id=f'{login.user_id}')

    assert_that(response.status_code).is_equal_to(200)
