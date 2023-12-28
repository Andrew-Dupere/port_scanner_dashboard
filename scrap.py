

import requests as r



url = 'http://18.118.218.230:8080/metrics'

rx = r.get(url)

rson = rx.json()

print(type(rx.json()))