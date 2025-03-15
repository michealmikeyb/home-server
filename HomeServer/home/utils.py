import asyncio
import os
from kasa import Discover
from kasa import SmartPlug
from tapo import ApiClient


SWITCHES = [
    {'alias': 'bedroom lights', 'ip': '10.32.65.122'}, 
    {'alias': 'string lights', 'ip': '10.32.65.153'}, 
    {'alias': 'Vape', 'ip': '10.32.65.129', 'tapo': True}
]

class TapoSwitchWrapper():
    def __init__(self, ip_address):
        self.client = get_tapo_client()
        self.tapo_device = asyncio.run(self.client.generic_device(ip_address))
        self.update()

    def update(self):
        self.device_info = asyncio.run(self.tapo_device.get_device_info())
        self.is_on = self.device_info.device_on
        self.alias = self.device_info.nickname

    def turn_on(self):
        return self.tapo_device.on()

    def turn_off(self):
        return self.tapo_device.off()

def get_switch(switch_name: str):
    found_devices = asyncio.run(Discover.discover())
    device = [dev for addr, dev in found_devices.items() if dev.alias == switch_name]
    if len(device) != 1:
        if switch_name not in [s['alias'] for s in SWITCHES]:
            raise ValueError("Invalid Name")
        s = [s for s in SWITCHES if s['alias'] == switch_name][0]
        if s.get('tapo'):
            return TapoSwitchWrapper(s['ip'])

        switch = SmartPlug(s['ip'])
        asyncio.run(switch.update())
        return switch
    return device[0]

def get_all_switches():
    found_devices = asyncio.run(Discover.discover())
    devices = [dev for addr, dev in found_devices.items()]
    if len(devices) == 0:
        for s in SWITCHES:
                if not s.get('tapo'): 
                    switch = SmartPlug(s['ip'])
                    asyncio.run(switch.update())
                    devices.append(switch)
    tapo_devices = [TapoSwitchWrapper(s['ip']) for s in SWITCHES if s.get('tapo')]
    devices.extend(tapo_devices)
    return devices

def get_tapo_client():
    tapo_username = os.getenv("TAPO_USERNAME")
    tapo_password = os.getenv("TAPO_PASSWORD")
    client = ApiClient(tapo_username, tapo_password)
    return client
