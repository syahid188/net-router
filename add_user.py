from sys import stderr, stdin, stdout
from ipaddress import ip_address
import paramiko, time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

#List of Ip Address
ipAddress = [
    "192.168.0.1",
    "192.168.0.2"
]

# Command yang akan di execute di terminal cli mikrotik
command = "user add name=syahid password=syahid group=write comment=IT-Syahid"

# Ganti hostname, port, username, password yang sesuai di ssh.connect()
for ip in ipAddress:
    ssh.connect(hostname=ip, port=22, username="admintest", password="rahasia")
    transport = ssh.get_transport()
    if transport is not None:
        print("SSH connection successful On IP " +ip+ "\n" )
    else:
        print("SSH connection failed.\n")
    time.sleep(2)
    try:
        ssh.exec_command(command)
    except Exception:
        print(Exception)
    stdin,stdout,stderr = ssh.exec_command("user print")
    print (stdout.read().decode("ascii").strip("\n"))
