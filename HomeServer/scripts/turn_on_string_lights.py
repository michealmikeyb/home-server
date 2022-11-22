from requests import Session
from threading import Thread


def turn_on_lights(light_name):
    sesh = Session()
    url = 'http://homeserver/switch'
    res = sesh.post(url=url, json={'name': light_name, 'command': 'on'}, verify=False)
    print(res.content)


if __name__ == '__main__':
    turn_on_lights('string lights')