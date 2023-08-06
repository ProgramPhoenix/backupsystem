import paramiko
import dotenv
import os

dotenv.load_dotenv()

host = os.getenv("host")
username = os.getenv("username")
keyfile = os.getenv("keyfile")

client = paramiko.client.SSHClient()
client.connect(hostname=host, username=username, key_filename=keyfile)

client.load_host_keys()

_stdin, _stdout,_stderr = client.exec_command("df")
print(_stdout.read().decode())

client.close()
