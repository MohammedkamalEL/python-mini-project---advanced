import requests
from pprint import PrettyPrinter

# BASE_URL = "https//data.nba.net"
BASE_URL = "https://jsonplaceholder.typicode.com/users/"
printt = PrettyPrinter()
# ALL_JSON = '/prod/v1/today.json'


def get_main():
    data = requests.get(BASE_URL).json()
    return data


def user_id(num):
    full_url = f"{BASE_URL}/{num}"
    data = requests.get(full_url).json()
    return data


# user = user_id(1)
# printt.pprint(user["company"])


def get_user_state(id):
    full_url = f"{BASE_URL}/{id}/todos"
    data = requests.get(full_url).json()
    team = list(filter(lambda x :x['completed'] == True ,data))
    fail = list(filter(lambda x: x["completed"] == False and len(x["title"]) > 10, data))
    title = list(map(lambda x: x["title"].upper(), data))
    return len(data), len(team), len(fail),title

all_todo, completed,fail, title = get_user_state(9)
score = completed / all_todo * 100
printt.pprint(f'all todo {all_todo} complet {completed}, and score is {score} -----> {fail}')
printt.pprint(title)


# duble_lamda = list(filter(lambda x: x <3 , [1, 2, 3, 4, 5]))

# print(duble_lamda)
