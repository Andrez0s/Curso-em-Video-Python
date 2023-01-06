# Crie um código em python que teste se o site pudim está acessível pelo computador usado:

import requests


def pudim():
    try:
        requests.get('http://www.pudim.com.br')
        return 'Site online!'
    except requests.ConnectionError:
        return 'Site Fora do ar'


print(pudim())
