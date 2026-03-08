import yaml
import socket
import logging

logging.basicConfig(
    filename="logs/reachability.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# Load devices from inventory
with open("inventory/devices.yaml") as f:
    devices = yaml.safe_load(f)["devices"]
port = 830

for device in devices:
    host = device["host"]

    try:
        with socket.create_connection((host, port), timeout=10):
            print(f"[✓] NETCONF reachable on {device['name']} ({host})")
            logging.info(f"NETCONF reachable on {device['name']} ({host})")

    except Exception as e:
        print(f"[x] Cannot reach {device['name']} ({host})")
        logging.error(f"Cannot reach {device['name']} ({host}): {e}")
