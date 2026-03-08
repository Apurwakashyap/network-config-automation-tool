# 🛠 Network Configuration Automation Tool

Python-based automation tool to configure network devices using NETCONF and YAML-based inventory.  
This project automates configuration deployment across multiple routers and includes device reachability checks and logging.

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
```bash
network-config-automation-tool/
│── configs/
│   └── interface_config.xml
│── inventory/
│   └── devices.yaml
│── logs/
│   └── config.log
│── main.py
│── report.py
├── check_devices.py
│── requirements.txt
│── README.md
│── .gitignore



---
```
## 🔧 Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/network-config-automation-tool.git
   cd network-config-automation-tool
   ```
2.Create a virtual environment(If want to  create virtual environment)

```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3.Install dependencies
pip install -r requirements.txt

```

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
