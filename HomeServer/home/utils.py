import asyncio
from kasa import Discover
from kasa import SmartPlug


SWITCHES = [
    {'alias': 'lamp', 'ip': '192.168.1.122'}, 
    {'alias': 'string lights', 'ip': '192.168.1.153'}
]

def get_switch(switch_name: str):
    found_devices = asyncio.run(Discover.discover())
    device = [dev for addr, dev in found_devices.items() if dev.alias == switch_name]
    if len(device) != 1:
        if switch_name not in [s['alias'] for s in SWITCHES]:
            raise ValueError("Invalid Name")
        s = [s for s in SWITCHES if s['alias'] == switch_name][0]
        switch = SmartPlug(s['ip'])
        asyncio.run(switch.update())
        return switch
    return device[0]

def get_all_switches():
    found_devices = asyncio.run(Discover.discover())
    devices = [dev for addr, dev in found_devices.items()]
    return devices
