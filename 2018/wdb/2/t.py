import sys
import time

print("")
sys.stdout.write("1\r")
sys.stdout.flush()
time.sleep(1)
sys.stdout.write("2\r")
sys.stdout.flush()
time.sleep(1)
sys.stdout.write("3\r")
print("3")
