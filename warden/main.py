import time

import requests

from warden.settings import INTERVAL, TIMEOUT, WEBHOOK, Logger


class IfConfig:
    name = "ifconfig.me"
    url = "http://ifconfig.me/all.json"

    def request(self):
        return requests.get(self.url, timeout=TIMEOUT)

    def get_ip(self):
        return self.request().json()["ip_addr"]


def trigger_notification(ip_address):
    message = {"content": f"Current minecraft IP address {ip_address}"}

    try:
        requests.post(WEBHOOK, data=message)
    except (requests.ConnectionError, requests.Timeout, requests.exceptions.HTTPError) as exc:
        Logger.info(f"Failed to notify with IP address: {exc}")
        return False
    else:
        return True


def monitor():
    Logger.info("Service initialized successfully")
    service = IfConfig()
    ip_address = service.get_ip()
    Logger.info(f"Starting IP address {ip_address}")
    trigger_notification(ip_address)
    while True:
        time.sleep(INTERVAL)
        try:
            current_ip_address = service.get_ip()
        except (requests.ConnectionError, requests.Timeout, requests.exceptions.HTTPError) as exc:
            Logger.info(f"Failed to fetch IP address: {exc}")
        else:
            Logger.debug(f"Fetched IP {current_ip_address}")
            if current_ip_address != ip_address:
                Logger.info(
                    "Detected IP change."
                    f"Current IP {current_ip_address}, Previous IP {ip_address}"
                )

                if trigger_notification(current_ip_address):
                    ip_address = current_ip_address


if __name__ == "__main__":
    monitor()
