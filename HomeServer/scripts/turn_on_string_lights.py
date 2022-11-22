from requests import Session
from threading import Thread


def turn_on_lights(light_name):
    csrf_key = 'X-CSRFToken'
    sesh = Session()
    url = 'https://gpmaga.com/switch'
    home_control_url = 'https://gpmaga.com/home-control'
    sesh.get(url=home_control_url, verify=False)
    threads = []
    t = Thread(
        target=sesh.post, 
        kwargs={
            'url': url, 
            'json': {'name': light_name, 'command': 'on'}, 
            'verify': False, 
            'headers': {csrf_key: sesh.cookies['csrftoken'], 'Referer': home_control_url}
            }
        )
    t.start()
    threads.append(t)
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    turn_on_lights('string lights')