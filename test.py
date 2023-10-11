import requests
import names
import uuid
import random

url = "https://gl5bphjsr4.execute-api.eu-west-1.amazonaws.com/api/"

def custom_random():
    rand_num = random.random()  # Generate a random float between 0 and 1

    if rand_num <= 0.60:
        return 1
    elif rand_num <= 0.85:
        return 2
    elif rand_num <= 0.95:
        return 3
    elif rand_num <= 0.99:
        return 4
    else:
        return 5

def buy_random():
    probability = 0.02
    random_number = random.random()
    if random_number < probability:
        return True
    else:
        return False


while True:
    email = names.get_full_name().replace(' ', '') + '@gmail.com'
    for api in ['android', 'ios', 'desktop']:
        postid = str(uuid.uuid4())
        for count in range(0, custom_random()):
            data = {'api': api, 'email': email, 'postid': postid}
            print(data)
            response = requests.post(url, json=data)
            print(response.json())
            if buy_random():
                data = {'api': 'transaction', 'email': email, 'postid': postid, 'amount_usd': random.randint(1, 1000)}
                print(data)
                response = requests.post(url, json=data)
                print(response.json())
