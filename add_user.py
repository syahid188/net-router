from sys import stderr, stdin, stdout
from ipaddress import ip_address
import paramiko, time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

#List of Ip Address
ipAddress = [
    "192.168.88.1",
    "192.168.88.2",
    "192.168.88.3"
]

# Command yang akan di execute di terminal cli mikrotik
command = "user add name=syahid password=syahid group=write comment=IT-Syahid"


# Ganti hostname, port, username, password yang sesuai di ssh.connect()
for ip in ipAddress:
    try:
        ssh.connect(hostname=ip, port=22, username="admintest", password="rahasia",timeout=5)
        print("SSH connection successful On IP " +ip+ "\n" )
        time.sleep(2)
        #Exec Command
        ssh.exec_command(command)
        stdin,stdout,stderr = ssh.exec_command("user print")
        print (stdout.read().decode("ascii").strip("\n"))
        time.sleep(2)
    except TimeoutError as e:
            print(f"Error: {e} connection on IP " +ip)
    except Exception:
        print(Exception)
    finally:
            ssh.close()