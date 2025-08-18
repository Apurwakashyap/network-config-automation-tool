import unittest
from ncclient import manager

class TestNetconfConnection(unittest.TestCase):
    def test_device_connection(self):
        device = {
            "host": "devnetsandboxiosxe.cisco.com",
            "port": 830,
            "username": "admin",
            "password": "C1sco12345",
            "hostkey_verify": False
        }
        try:
            with manager.connect(**device) as m:
                self.assertTrue(m.connected)
        except Exception as e:
            self.fail(f"Connection failed: {e}")

if __name__ == '__main__':
    unittest.main()
