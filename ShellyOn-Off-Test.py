import requests
from time import sleep

def turn_shelly_on(ip_address):
    sleep(3)
    url = f'http://{ip_address}/relay/0?turn=on'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Shelly is turned on.")
            return True
        else:
            print(f"Failed to turn Shelly on. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def turn_shelly_off(ip_address):
    sleep(3)
    url = f'http://{ip_address}/relay/0?turn=off'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Shelly is turned off.")
            return True
        else:
            print(f"Failed to turn Shelly off. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    shelly_ip = "192.168.xxx.xxx"  # Replace with your Shelly device's IP address

    # Turn Shelly on
    if turn_shelly_on(shelly_ip):
        print("Successfully turned Shelly on")

    # Turn Shelly off
    if turn_shelly_off(shelly_ip):
        print("Successfully turned Shelly off")
