## User Lottery's
import requests 

resp = requests.get('https://randomuser.me/api/?results=100')

data = resp.json()

perfil = data['results'][0]

### Identificar o perfil
##
# afim de avaliar as informações presentes no json, sobre o perfil de cada usuario

for user in data['results'][:1]:
    print(user['name']['first'],':', '\n')
    for ctg in perfil:
        print('\n','-',ctg,'\n')

