from requests import Session
from threading import Thread


def turn_off_lights():
    csrf_key = 'X-CSRFToken'
    sesh = Session()
    url = 'https://gpmaga.com/switch'
    home_control_url = 'https://gpmaga.com/home-control'
    sesh.get(url=home_control_url, verify=False)
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
                    'verify': False, 
                    'headers': {csrf_key: sesh.cookies['csrftoken'], 'Referer': home_control_url}
                    }
                )
            t.start()
            threads.append(t)
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    turn_off_lights()