import os
import platform
import socket
def determine_platform() -> tuple[str, str]:
    name = os.name
    plat = platform.system()
    return name, plat

def get_computer_name() -> str:
    return socket.gethostname()

if __name__ == "__main__":
    print(get_computer_name())
