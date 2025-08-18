from ncclient import manager

device = {
    "host": "devnetsandboxiosxe.cisco.com",
    "port": 830,
    "username": "admin",
    "password": "C1sco12345",
    "hostkey_verify": False
}

try:
    with manager.connect(**device) as m:
        print("Successfully connected to Netconf!")
        # To check capabilities:
        print("Netconf Capabilities:", m.server_capabilities)
except Exception as e:
    print(f"Error: {e}")
