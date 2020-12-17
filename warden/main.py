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
    requests.post(WEBHOOK, data=message)


def monitor():
    Logger.info("Service initialized successfully")
    service = IfConfig()
    ip_address = service.get_ip()
    Logger.info(f"Starting IP address {ip_address}")
    while True:
        time.sleep(INTERVAL)

        current_ip_address = service.get_ip()
        Logger.debug(f"Fetched IP {current_ip_address}")
        if current_ip_address != ip_address:
            Logger.info(
                "Detected IP change."
                f"Current IP {current_ip_address}, Previous IP {ip_address}"
            )
            ip_address = current_ip_address
            trigger_notification(ip_address)


if __name__ == "__main__":
    monitor()
