import os
import requests

api_address = '172.17.0.1'  
api_port = 8000


positive_sentence = 'life is beautiful'
negative_sentence = 'that sucks'
api_port = 8000

def perform_test(endpoint):
    r = requests.get(
        url=f'http://{api_address}:{api_port}/{endpoint}',
        params={
            'username': 'alice',
            'password': 'wonderland',
            'sentence': positive_sentence if 'v2' in endpoint else negative_sentence
        }
    )

    output = f'''
    ============================
        Content test - {endpoint}
    ============================
    request done at "{endpoint}"
    | username="alice"
    | password="wonderland"
    | sentence="{positive_sentence if 'v2' in endpoint else negative_sentence}"
    
    expected result positive = {"TRUE" if 'v2' in endpoint else "FALSE"}
    actual result positive = {"TRUE" if r.json()["score"] > 0 else "FALSE"}
    score value = {r.json()["score"]}
    ==>  {"SUCCESS" if ('v2' in endpoint and r.json()["score"] > 0) or ('v1' in endpoint and r.json()["score"] < 0) else "FAILURE"}
    '''

    print(output)

    if os.environ.get('LOG') == '1':
        with open('../my_log/api_test.log', 'a+') as file:
            file.write(output)

perform_test('v2/sentiment')
perform_test('v1/sentiment')