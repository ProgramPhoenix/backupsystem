import dotenv
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


sshProcess = subprocess.Popen(['ssh',
                               '-i',
                               keyfile,
                               username + "@" + host],
                               stdin=subprocess.PIPE,
                               stdout = subprocess.PIPE,
                               universal_newlines=True,
                               bufsize=0)
sshProcess.stdin.write("ls")
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