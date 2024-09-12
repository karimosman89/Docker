import os
import requests

api_address = '172.17.0.1'  
api_port = 8000

users = [
    {'username': 'alice', 'password': 'wonderland'},
    {'username': 'bob', 'password': 'builder'},
    {'username': 'clementine', 'password': 'mandarine'}
]

for user in users:
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params=user
    )
    output = f'''
    ============================
        Authentication test
    ============================
    request done at "/permissions"
    | username="{user['username']}"
    | password="{user['password']}"
    expected result = 200
    actual result = {r.status_code}
    ==>  { 'SUCCESS' if r.status_code == 200 else 'FAILURE'}
    '''
    print(output)
    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(output)
