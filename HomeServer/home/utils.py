import asyncio
from kasa import Discover


def get_switch(switch_name: str):
    found_devices = asyncio.run(Discover.discover())
    device = [dev for addr, dev in found_devices.items() if dev.alias == switch_name]
    if len(device) != 1:
        raise ValueError("Invalid Name")
    return device[0]

def get_all_switches():
    found_devices = asyncio.run(Discover.discover())
    devices = [dev for addr, dev in found_devices.items()]
    return devices
