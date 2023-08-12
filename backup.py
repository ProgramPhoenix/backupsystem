import dotenv
import paramiko
import os
import logging
import subprocess

logging.basicConfig()
logging.getLogger("paramiko").setLevel(logging.DEBUG)

dotenv.load_dotenv()

host = os.getenv("host")
username = os.getenv("user")
keyfile = os.getenv("keyfile")
password = os.getenv("password")

ssh = paramiko.SSHClient()
k = paramiko.RSAKey.from_private_key_file(keyfile)
# OR k = paramiko.DSSKey.from_private_key_file(keyfilename)

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=username, pkey=k)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ls")
print( ssh_stdin.readline())
ssh.close()


'''
sshProcess = subprocess.Popen(['ssh',
                               '-i',
                               keyfile,
                               username + "@" + host],
                               stdin=subprocess.PIPE,
                               stdout = subprocess.PIPE,
                               universal_newlines=True,
                               bufsize=0)

sshProcess.stdout.flush()

sshProcess.stdin.write("ls\n")
sshProcess.stdin.write("echo END\n")
sshProcess.stdin.write("uptime\n")
sshProcess.stdin.write("logout\n")
sshProcess.stdin.close()


for line in sshProcess.stdout:
    if line == "END\n":
        break
    print(line, end="")

#to catch the lines up to logout
for line in  sshProcess.stdout:
    print(line, end="")
'''