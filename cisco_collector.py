import yaml
from scrapli.driver.core import IOSXEDriver


def main():
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    for device_name, device_config in config.items():
        commands = device_config.pop("commands")

        with IOSXEDriver(**device_config) as conn, \
            open(f"output/{device_name}.txt", mode="w") as f:
            for command in commands:
                f.write("\n\n{:=^80}\n{:^80}\n{:=^80}\n\n".format("", command, ""))
                result = conn.send_command(command)
                f.write(result.result)

        print(f"Device {device_name} saved in {device_name}.txt file")


if __name__ == "__main__":
    main()
