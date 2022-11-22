from requests import Session
from threading import Thread


def turn_on_lights(light_name):
    csrf_key = 'X-CSRFToken'
    sesh = Session()
    url = 'http://homeserver/switch'
    home_control_url = 'http://homeserver/home-control'
    sesh.get(url=home_control_url, verify=False)
    res = sesh.post(url=url, json={'name': light_name, 'command': 'on'}, verify=False, headers={csrf_key: sesh.cookies['csrftoken'], 'Referer': home_control_url})
    print(res.content)


if __name__ == '__main__':
    turn_on_lights('string lights')