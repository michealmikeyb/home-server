from requests import Session
from threading import Thread
import time
import datetime
import pytz
from astral import LocationInfo
from astral.sun import sun

# Choose your location for sunrise/sunset calculations                          
MY_TIMEZONE = "America/Los_Angeles"
MY_LONGITUDE = '37.7833'  # +N
MY_LATITUDE = '-122.4167' # +E
MY_ELEVATION = 0          # meters   

# Choose when to start and stop relative to sunrise and sunset                  
START_AFTER_SUNSET_MIN = 10
WAIT_INTERVAL = 300

def turn_on_lights(light_name):
    csrf_key = 'X-CSRFToken'
    sesh = Session()
    url = 'http://homeserver/switch'
    home_control_url = 'http://homeserver/home-control'
    res = sesh.get(url=home_control_url, verify=False)
    print(res.content)
    res = sesh.post(url=url, json={'name': light_name, 'command': 'on'}, verify=False, headers={csrf_key: sesh.cookies['csrftoken'], 'Referer': home_control_url})
    print(res.content)
                                                                                                         

def main():                                                                     
  # Configure the timezone    
  tz = pytz.timezone(MY_TIMEZONE)                                                    
  loc = LocationInfo(name='SJC', region='CA, USA', timezone=pytz.UTC,
                   latitude=37.3713439, longitude=-121.944675)
  s = sun(loc.observer, date=datetime.datetime.now().date(), tzinfo=tz)
  sunset = s['sunset']
  start_time = sunset + datetime.timedelta(minutes=START_AFTER_SUNSET_MIN)
  while datetime.datetime.now(tz=tz) < start_time:
    print(f'waiting {START_AFTER_SUNSET_MIN} minutes after sunset at {start_time}...')                                             
    time.sleep(WAIT_INTERVAL)
  print('turning on string lights')
  turn_on_lights('string lights')                                                            

if __name__ == '__main__':                                                      
  main()