class Mainsetting:
    url ='https://spot-api.moco.co.id'

class Login:
    # variable positive test
    txtEmail = 'sarjiman@grr.la'
    txtPassword = 'huhu12345'

    # variable login with token
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJhY2Nlc3M6NjE1NjdjZDYtMWI0NS00NTM1LThiMDUtODJmZGRhNzQwNDU3Iiwic3ViIjoiMmVkYjY2YjUtODM5OS00Y2NmLTg2NWEtNWI1OWI2NDM5NWY5IiwiaWF0IjoxNzI3OTY5Mzg5LCJleHAiOjE3Mjc5NzI5ODksImF1ZCI6Iks2OFA0SjZLIiwiaXNzIjoiYWRtaW4ifQ.khKQWQ9kA2-rZe3Sxd7pftUL92pFRvsdEKOxJs105-w'
    organization_id = '2eb04da6-a56d-475b-ab6f-2984bab884ad'
    user_id = '2edb66b5-8399-4ccf-865a-5b59b64395f9'

    # variable negative test
    list_login_negatif = ({
        'data1':{
        'email':'sarjiman@grr.la',
        'password':'huhuhaha',
        'pesan':'Password tidak sesuai.'
        },
        'data2':{
        'email':'sarjiman@grr.laa',
        'password':'huhu12345',
        'pesan':'Pengguna tidak ditemukan.'
        },
        'data3':{
        'email':'sarjiman@grr.laa',
        'password':'huhuhaha',
        'pesan':'Pengguna tidak ditemukan.'
        }
    })


    # variable notfound
    notfound_login={
        'email':'sarjana@grr.la',
        'password':'sarjana'
    }
class DetailBook:
    pass
