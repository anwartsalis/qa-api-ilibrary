from assertpy import assert_that

from setting import Mainsetting
from setting import Login
import requests
import  pytest

main_setting = Mainsetting
login = Login
url_login = f'{main_setting.url}/backend/auth/login'
def test_post_login_positif() :
    payload = {'email':f'{login.txtEmail}','password':f'{login.txtPassword}'}
    response = requests.post(url_login,json=payload)

    # assertion
    assert_that(response.status_code).is_equal_to(200)

data = login.list_login_negatif
input_result =[
    (f'{data['data1']['email']}',f'{data['data1']['password']}',f'{data['data1']['pesan']}'),
    (f'{data['data2']['email']}',f'{data['data2']['password']}',f'{data['data2']['pesan']}'),
    (f'{data['data3']['email']}',f'{data['data3']['password']}',f'{data['data3']['pesan']}')
]

@pytest.mark.parametrize('email,password,message',input_result)
def test_post_login_negatif(email,password,message):
    '''
    skenario negatif tes login:
    email       password    result
    benar       salah       Password tidak sesuai.
    salah       benar       Pengguna tidak ditemukan.
    salah       salah       Pengguna tidak ditemukan.
    '''
    # page_main = main_setting.url
    payload = {'email': f'{email}', 'password': f'{password}'}
    response = requests.post(url_login, json=payload)

    # assertion
    assert_that(response.status_code).is_equal_to(401)
    assert_that(message).is_equal_to(response.json()['error']['message'])
    print(response.text)

def test_post_login_with_token():
    payload ={'token':f'{login.token}','organization_id':f'{login.organization_id}','user_id':f'{login.user_id}','email':f'{login.txtEmail}','password':f'{login.txtPassword}'}
    response = requests.post(url_login,json=payload)
    print(response.text)

    # assertion
    assert response.status_code == 200

def test_post_login_notfound():
    notfound = login.notfound_login
    payload = {'email':f'{notfound['email']}','password':f'{notfound['password']}'}
    response = requests.post(url_login,json=payload)
    print(response.text)

    # assertion
    assert response.status_code == 401