"""PY_TEST_SCR.py"""
import os
import sys
import platform
from datetime import datetime
from random import randint
import socket
#from pip import _internal

print(f'| Current DT :: {datetime.now()} |')
print(f'| sys.v :: {sys.version} |')
print(f'| platform.v :: {platform.python_version()} |')
print(f'| Executable :: {os.path.dirname(sys.executable), sys.executable} |')
print(f'| randint :: {randint(0, 100)} |')
print(f'| User @ Host :: {os.getlogin()}@{socket.gethostname()} |')

#print(os.system('ip a'))
