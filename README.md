#**Bluesafe**


Bluesafe is a python script that checks your connected bluetooth devices,
in case your predefined device gets disconnected your laptop will restart
to encrypt your disk.

##**Usage**

Create a cronjob or a service that runs bluesafe.py everytime your laptop reboots.

Edit the lock_device option at the top of the file with the mac address of your bluetooth
device, example lock_device = "AA:BB:CC:DD:EE:FF"


everytime the script is run it is set to be unarmed, after you connect your bluetooth the device
the script gets armed and in case of a disconnection your laptop will reboot securing your data.

