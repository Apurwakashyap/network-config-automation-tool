# 🛠 Network Configuration Automation Tool

Python-based automation tool to configure network devices using NETCONF and YAML-based inventory.  
This project automates configuration deployment across multiple routers and includes device reachability checks and logging.

---

## 🧰 Technologies Used

- Python
- YAML
- NETCONF
- ncclient
- Socket Programming
  
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
│
├── configs/
│   └── interface_config.xml
├── inventory/
│   └── devices.yaml
├── logs/
│   └── config.log
├── main.py
├── report.py
├── check_devices.py
├── requirements.txt
├── .gitignore
└── README.md
---
```
## 🔧 Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/Apurwakashyap/network-config-automation-tool.git
   cd network-config-automation-tool
   ```
2.*Create a virtual environment(If want to  create virtual environment)*

```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

```
3.**Install dependencies**
```bash
pip install -r requirements.txt
```

      
⚙️ Configuration
1.Device Inventory (inventory/devices.yaml)
Define the devices you want to configure:
```yaml

devices:
  - name: router1
    host: <router-ip>
    port: 830
    username: <username>
    password: <password>
    hostkey_verify: false
```
- **name** – Device identifier
- **host** – Router IP address
- **port** – NETCONF port (default 830)
- **username/password** – Device credentials
- **hostkey_verify** – Disable SSH host key verification


## ⚙️ Automation Workflow

1. Check device connectivity

    python check_devices.py

2. Deploy configuration

    python main.py

3. View logs

   logs/config.log

📖 References
Cisco DevNet Sandbox
