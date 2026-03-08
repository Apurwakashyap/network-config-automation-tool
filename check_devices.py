import yaml
import socket

NETCONF_PORT = 830

# Load devices from inventory
with open("inventory/devices.yaml") as f:
    devices = yaml.safe_load(f)["devices"]

print("\nChecking device connectivity...\n")

for device in devices:
    host = device["host"]

    try:
        with socket.create_connection((host, NETCONF_PORT), timeout=5):
            print(f"[✓] {device['name']} ({host}) - NETCONF reachable")
    except Exception:
        print(f"[x] {device['name']} ({host}) - NETCONF NOT reachable")

print("\nConnectivity check complete.\n")
