import time

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
'''
ssh = paramiko.SSHClient()
k = paramiko.RSAKey.from_private_key_file(keyfile)
# OR k = paramiko.DSSKey.from_private_key_file(keyfilename)

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=username, pkey=k, timeout=None)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("nohup zip -r backup_vol.zip volumes &", get_pty=True, timeout=None)

while not ssh_stdout.channel.exit_status_ready():
    print("sleep")
    time.sleep(10)

print(ssh_stdout.channel.recv_exit_status())
ssh_stdin.close()
ssh_stdout.close()
ssh_stderr.close()
ssh.close()
'''
command = "zip -r backup_vol.zip volumes & "

sshProcess = subprocess.Popen(['ssh',
                               '-i',
                               keyfile,
                               username + "@" + host,
                               command])

while sshProcess.poll() is None:
    print("running")
    time.sleep(10)

scpProcess = subprocess.Popen(['scp',
                               '-i',
                               keyfile,
                               username + "@" + host + ":/root/backup_vol.zip",
                               "/home/programphoenix/backup"])

while scpProcess.poll() is None:
    print("running")
    time.sleep(10)

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