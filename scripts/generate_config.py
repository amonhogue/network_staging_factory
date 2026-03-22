import os
import sys
from pathlib import Path

import pynetbox
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    load_dotenv(dotenv_path=base_dir / ".env")

    netbox_url = os.getenv("NETBOX_URL")
    netbox_token = os.getenv("NETBOX_TOKEN")

    if not netbox_url or not netbox_token:
        raise ValueError("NETBOX_URL or NETBOX_TOKEN is missing")

    device_name = sys.argv[1] if len(sys.argv) > 1 else "lab-ex-01"

    nb = pynetbox.api(netbox_url, token=netbox_token)
    device = nb.dcim.devices.get(name=device_name)

    if not device:
        raise ValueError(f"Device {device_name} not found")

    if not device.primary_ip4:
        raise ValueError(f"Device {device_name} has no primary IPv4")

    hostname = device.name
    mgmt_ip = device.primary_ip4.address

    template_dir = base_dir / "templates"
    output_dir = base_dir / "generated-configs"
    output_dir.mkdir(exist_ok=True)

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("junos_base.j2")

    rendered = template.render(
        hostname=hostname,
        mgmt_ip=mgmt_ip,
    )

    output_file = output_dir / f"{hostname}.conf"
    output_file.write_text(rendered)

    print(f"Device: {hostname}")
    print(f"Management IP: {mgmt_ip}")
    print(f"Config generated: {output_file}")


if __name__ == "__main__":
    main()
