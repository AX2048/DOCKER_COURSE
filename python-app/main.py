import calendar
import os, sys, platform
from datetime import datetime
from random import randint
import socket
#from pip import _internal

print('Добро пожаловать в супер календарь')

year = int(input('Введите год: '))
month = int(input('Введите месяц: '))

print(calendar.month(year, month))

print('Всего хорошего!')




current_datetime = datetime.now()
r = randint(0, 25)


print(f'| sys.v :: {sys.version} |')
print(f'| platform.v :: {platform.python_version()} |')
print(f'| Executable :: {os.path.dirname(sys.executable), sys.executable} |')
print(f'| randint :: {r} |')
#print(f'| User @ Host :: {os.getlogin()}@{socket.gethostname()} |')

#print(os.system('ip a'))