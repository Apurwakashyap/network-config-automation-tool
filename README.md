# 🛠 Network Configuration Automation Tool

This project automates **network device configuration** using **NETCONF** and **YANG** models.  
It connects to devices (like Cisco IOS-XE) via `ncclient` and applies pre-defined XML/YANG configurations.  
A simple reporting script is also included to verify device connectivity.

---

## 🚀 Features
- Automates pushing configurations to multiple devices
- Uses **NETCONF (port 830)** for configuration management
- Reads device inventory from YAML file
- Applies XML-based interface configuration
- Logs success & errors in `logs/config.log`
- Includes a **reporting utility** to check device reachability

---

## 📂 Project Structure
network-config-automation-tool/
│── configs/
│   └── interface_config.xml
│── inventory/
│   └── devices.yaml
│── logs/
│   └── config.log
│── main.py
│── report.py
│── requirements.txt
│── README.md
│── .gitignore



---

## 🔧 Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/network-config-automation-tool.git
   cd network-config-automation-tool
2.Create a virtual environment(If want to  create virtual environment)

python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3.Install dependencies
pip install -r requirements.txt


⚙️ Configuration
1. Device Inventory (inventory/devices.yaml)
Define the devices you want to configure:

devices:
  - name: iosxe-router
    host: devnetsandboxiosxe.cisco.com
    port: 830
    username: developer
    password: C1sco12345
    hostkey_verify: false

▶️ Usage
Run the automation script
python main.py

✅ Requirements
Python 3.x

Libraries:

ncclient

PyYAML

pytest (for testing)


📖 References
Cisco DevNet Sandbox
