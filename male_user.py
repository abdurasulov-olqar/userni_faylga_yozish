import requests
import json

users = []
while len(users)<=50:

    response = requests.get('https://randomuser.me/api/')

    if response.status_code == 200:
        data = json.loads(response.text)
        results = data['results']
        name = data['results'][0]['name']
        if results[0]['gender'] == 'male':
            full_name = f'{name["first"]} {name["last"]}'
            country = results[0]['location']['country']
            phone = results[0]['phone']
            gender = results[0]['gender']

            user = {
                'fullname': full_name,
                'country': country,
                'phone': phone,
                'gender': gender
            }

            users.append(user)
        
js = json.dumps(users)
f = open("male_user.json", "w")
f.write(js)
f.close()