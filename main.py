import yaml
from ncclient import manager
import logging

# Setup logging
logging.basicConfig
(filename="logs/config.log", 
level=logging.INFO,
format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load devices from YAML
with open("inventory/devices.yaml") as f:
    devices = yaml.safe_load(f)["devices"]

# Load XML config
with open("configs/interface_config.xml") as f:
    config_payload = f.read()

# Connect and apply config
for device in devices:
    try:
        # Copy the device dictionary but remove the 'name' key
        conn_params = {k: v for k, v in device.items() if k != "name"}

         with manager.connect(timeout=30, **conn_params) as m:
            m.edit_config(target="running", config=config_payload)
            logging.info(f"Successfully configured {device['name']}")
            print(f"[✓] Configured {device['name']}")
    except Exception as e:
        logging.error(f"Error configuring {device['name']}: {e}")
        print(f"[x] Failed to configure {device['name']}: {e}")
