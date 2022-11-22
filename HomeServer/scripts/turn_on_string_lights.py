from requests import Session
from threading import Thread


def turn_on_lights(light_name):
    sesh = Session()
    url = 'http://homeserver/switch'
    threads = []
    t = Thread(
        target=sesh.post, 
        kwargs={
            'url': url, 
            'json': {'name': light_name, 'command': 'on'}, 
            'verify': False, 
            }
        )
    t.start()
    threads.append(t)
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    turn_on_lights('string lights')