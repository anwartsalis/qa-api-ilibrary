from setting import Mainsetting
import requests
import  pytest

main_setting = Mainsetting

def test_get_data_book():
    main_url = main_setting.url
    # token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJhY2Nlc3M6NjE1NjdjZDYtMWI0NS00NTM1LThiMDUtODJmZGRhNzQwNDU3Iiwic3ViIjoiMmVkYjY2YjUtODM5OS00Y2NmLTg2NWEtNWI1OWI2NDM5NWY5IiwiaWF0IjoxNzI3OTY5Mzg5LCJleHAiOjE3Mjc5NzI5ODksImF1ZCI6Iks2OFA0SjZLIiwiaXNzIjoiYWRtaW4ifQ.khKQWQ9kA2-rZe3Sxd7pftUL92pFRvsdEKOxJs105-w'
    header = {'Authorization': 'Bearer token = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJhY2Nlc3M6NjE1NjdjZDYtMWI0NS00NTM1LThiMDUtODJmZGRhNzQwNDU3Iiwic3ViIjoiMmVkYjY2YjUtODM5OS00Y2NmLTg2NWEtNWI1OWI2NDM5NWY5IiwiaWF0IjoxNzI3OTY5Mzg5LCJleHAiOjE3Mjc5NzI5ODksImF1ZCI6Iks2OFA0SjZLIiwiaXNzIjoiYWRtaW4ifQ.khKQWQ9kA2-rZe3Sxd7pftUL92pFRvsdEKOxJs105-w'}
    book_id = {'id':'ebd48961-f188-4692-9db1-46a6dd1fd462'}
    response = requests.get(f'{main_url}/backend/webhook/book-detail/',headers=header,params=book_id)
    print(response.text)
    # assert response.status_code == 200