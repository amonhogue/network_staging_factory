from jnpr.junos import Device
from jnpr.junos.utils.config import Config

DEVICE_IP = "192.168.100.3"
USERNAME = "lab"
PASSWORD = "lab"
CONFIG_FILE = "generated-configs/lab-ex-01.conf"


def main():
    print(f"Connecting to {DEVICE_IP}...")

    with Device(host=DEVICE_IP, user=USERNAME, passwd=PASSWORD) as dev:
        cu = Config(dev)

        print("Loading configuration...")
        cu.load(path=CONFIG_FILE, format="text", merge=True)

        print("Performing commit check...")
        cu.commit_check()

        print("Committing configuration...")
        cu.commit()

        print("Configuration applied successfully.")


if __name__ == "__main__":
    main()
