import requests
import json,os


def upload(path):
    headers = {'Authorization': '4p7X1b1FJIvoMqR0CUysKf3blXp5hUrL'}
    files = {'smfile': open(path, 'rb')}
    url = 'https://sm.ms/api/v2/upload'
    res = requests.post(url, files=files,headers='').json()
    print(type(res))
    print(type(json.loads(res)))


if __name__ == "__main__":
    os.makedirs('./temp/2020/09/16')
