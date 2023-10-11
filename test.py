import requests
import names
import uuid


url = "https://8z2wlnzo58.execute-api.eu-west-1.amazonaws.com/api/"



while True:
    email = names.get_full_name().replace(' ', '') + '@gmail.com'
    for api in ['vehicle', 'real-estate', 'jobs']:
        data = {'api': api, 'email': email, 'postId': str(uuid.uuid4())}
        print(data)
        #response = requests.post(url, json=data)
        #print(response.json())
