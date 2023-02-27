"""PY_TEST_SCR.py"""
import os
import sys
import platform
from datetime import datetime
from random import randint
import socket


print(f'| Current DT :: {datetime.now()} |')
print(f'| sys.v :: {sys.version} |')
print(f'| platform.v :: {platform.python_version()} |')
print(f'| Executable :: {os.path.dirname(sys.executable), sys.executable} |')
print(f'| randint :: {randint(0, 100)} |')
print(f'| User @ Host :: {os.getlogin()}@{socket.gethostname()} |')

print('')

# Get the operating system name
os_name = platform.system()

# Get the operating system version
os_version = platform.release()

# Get the operating system architecture
os_architecture = platform.machine()

# Print the OS information
print(f"| Operating System: {os_name} |")
print(f"| Version: {os_version} |")
print(f"| Architecture: {os_architecture} |")