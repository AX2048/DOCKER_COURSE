"""docstring"""
import calendar
import os
import sys
import platform
from datetime import datetime
from random import randint
#import socket

print('Добро пожаловать в супер календарь')

year = int(input('Введите год: '))
month = int(input('Введите месяц: '))

print(calendar.month(year, month))

print('Всего хорошего!')

print(f'| Current DT :: {datetime.now()} |')
print(f'| sys.v :: {sys.version} |')
print(f'| platform.v :: {platform.python_version()} |')
print(f'| Executable :: {os.path.dirname(sys.executable), sys.executable} |')
print(f'| randint :: {randint(0, 100)} |')
#print(f'| User @ Host :: {os.getlogin()}@{socket.gethostname()} |')
#use docker run -e LOGNAME -it my-calendar:4.1.0 for os.getlogin()
