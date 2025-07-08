# Create rssi_sender.py on Each RPi
import requests
import time
from bluepy.btle import Scanner

NGROK_URL = "https://1234abcd.ngrok.io/rssi"

RPi_ID = "RPi-A"  # Change to "RPi-B" on the second Raspberry Pi
TARGET_DEVICE_MAC = "XX:XX:XX:XX:XX:XX"  # mobile BLE MAC address

def scan_for_device(mac_addr):
    scanner = Scanner()
    devices = scanner.scan(3.0)  # 3-second BLE scan
    for dev in devices:
        if dev.addr.lower() == mac_addr.lower():
            return dev.rssi
    return None

while True:
    rssi = scan_for_device(TARGET_DEVICE_MAC)
    if rssi is not None:
        data = {"rpi": RPi_ID, "rssi": rssi}
        try:
            res = requests.post(NGROK_URL, json=data)
            print(f"Sent {rssi} dBm from {RPi_ID}")
        except Exception as e:
            print(f"Error sending data: {e}")
    else:
        print(f"{RPi_ID} couldn't find target device.")
    time.sleep(2)