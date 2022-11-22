from requests import Session
from threading import Thread


def turn_off_lights():
    sesh = Session()
    url = 'http://homeserver/switch'
    res = sesh.get(url=url, verify=False)
    switches = res.json()['switches']
    threads = []
    for switch in switches:
        if switch["is_on"]:
            t = Thread(
                target=sesh.post, 
                kwargs={
                    'url': url, 
                    'json': {'name': switch['name'], 'command': 'off'}, 
                    'verify': False
                    }
                )
            t.start()
            threads.append(t)
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    turn_off_lights()