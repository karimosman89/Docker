
import os
import requests

api_address = '172.17.0.1'   
api_port = 8000




def perform_test(username, password, sentence, endpoint, expected_code):
    r = requests.get(
        url=f'http://{api_address}:8000/{endpoint}',
        params={
            'username': username,
            'password': password,
            'sentence': sentence
        }
    )

    output = f'''
    ============================
        Authorization test - {username} for {endpoint}
    ============================
    request done at "{endpoint}"
    | username="{username}"
    | password="{password}"
    | sentence="{sentence}"
    
    expected result = {expected_code}
    actual result = {r.status_code}

    ==>  {"SUCCESS" if r.status_code == expected_code else "FAILURE"}
    '''

    print(output)

    if os.environ.get('LOG') == '1':
        with open('../logs/api_test.log', 'a') as file:
            file.write(output)

alice_sentence = ['Both Versions']
bob_sentence = ['Just Version 1']


perform_test('alice', 'wonderland', alice_sentence, 'v1/sentiment', 200)
perform_test('alice', 'wonderland', alice_sentence, 'v2/sentiment', 200)


perform_test('bob', 'builder', bob_sentence, 'v1/sentiment', 200)
perform_test('bob', 'builder', bob_sentence, 'v2/sentiment', 403)
