print("ola do Python ao mudo")

import os
import socket
import platform

branch = os.getenv("GITHUB_REF")
hostname = socket.gethostname()
sistem = platform.system()

print(f"Branch: {branch} - hostname: {hostname} - Sitema: {sistem}")

