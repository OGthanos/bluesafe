import pydbus
import time
import os

lock_device = ""

bus = pydbus.SystemBus()
adapter = bus.get('org.bluez', '/org/bluez/hci0')
mngr = bus.get('org.bluez', '/')
armed = False

def list_connected_devices():
    mngd_objs = mngr.GetManagedObjects()
    for path in mngd_objs:
        con_state = mngd_objs[path].get('org.bluez.Device1', {}).get('Connected', False)
        if con_state:
            addr = mngd_objs[path].get('org.bluez.Device1', {}).get('Address')
            name = mngd_objs[path].get('org.bluez.Device1', {}).get('Name')
            return addr

if __name__ == '__main__':
    while 1:
        device = list_connected_devices()
        if device == lock_device:
            armed= True
        else:
            if armed == True:
                os.system("reboot")

        time.sleep(5)

