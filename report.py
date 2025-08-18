import socket

host = "devnetsandboxiosxe.cisco.com"
port = 830

# Try to connect to the device on port 830
try:
    with socket.create_connection((host, port), timeout=10):
        print(f"Port {port} is open on {host}")
except (socket.timeout, socket.error) as e:
    print(f"Could not connect to {host} on port {port}: {e}")
