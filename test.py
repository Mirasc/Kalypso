import requests
import json


def upload(path):
    headers = {'Authorization': '4p7X1b1FJIvoMqR0CUysKf3blXp5hUrL'}
    files = {'smfile': open(path, 'rb')}
    url = 'https://sm.ms/api/v2/upload'
    res = requests.post(url, files=files, headers=headers).json()
    print(json.dumps(res, indent=4))


if __name__ == "__main__":
    upload('tttt.png')