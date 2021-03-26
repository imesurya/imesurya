from subprocess import Popen, STDOUT, PIPE
from time import sleep
import os, getpass

print('Your available wifi networks are:')
os.system('nmcli dev wifi list')
input1 = input('Your choice?')
handle = Popen(input1, stdout=PIPE, stdin=PIPE, shell=True,  stderr=STDOUT)

password = getpass.getpass('Passowrd:')

handle.stdin.write(str.encode(password))
if handle.poll() == None:
    print(handle.stdout.readline().strip())
else:
    print('connected')