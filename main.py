import requests
import json

def get_auth_token(task_name):
    URL = f"https://zadania.aidevs.pl/token/{task_name}"
    data = {"apikey": "caadaf59-3666-4879-aaf8-7ad52df4c407"}
    request = requests.post(URL, json=data)
    return request.json().get('token')

def get_lesson(token):
    URL = f"https://zadania.aidevs.pl/task/{token}"
    result = requests.get(URL)
    print(result)
    print(result.json())

def answer_lesson(answer):
    URL = f"https://zadania.aidevs.pl/answer/{answer}"

def main(task_name):
    token = get_auth_token(task_name)
    lesson = get_lesson(token)
    print(lesson)

if __name__ == '__main__':
    main("helloapi")


