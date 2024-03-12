# The paramiko module to establish an SSHv2 connection I hope you like it and any suggestions will be highly considered specially how to beautify and make the output of the ssh human-readable

# A module for the ssh connection
import paramiko 
from time import sleep 
from pwinput import pwinput 
import sys
from pprint import pprint

host_val = input('Enter the hostname: ')
user_val = input('Enter the username: ')
passcode = pwinput(prompt = 'Enter the password: ', mask = '*')

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=host_val, username=user_val, password=passcode, look_for_keys=False, allow_agent=False)
    print(f"Connection Established with {user_val} : {host_val}")
    ssh = client.invoke_shell()
except Exception as e:
    print(f"Connection is not established: Detail: {e}")
    sys.exit(1)

while True:
    message = input('$> ')
    msg = message + '\n'
    ssh.send(msg)
    sleep(2)
    pprint(ssh.recv(3000))
    if message.endswith('rawley'):
        print(f"Connection Closed")
        break  

ssh.close()
