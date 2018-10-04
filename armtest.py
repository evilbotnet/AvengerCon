#!/usr/bin/python3
from subprocess import check_output
import subprocess
import sys
import os
import signal

#def get_pid(name):
#        return check_output(["pidof",name]).decode("utf-8").strip('\n').split(" ")


app = "/usr/bin/python3"
motion = "/home/pi/Pimoroni/envirophat/examples/motion_detect.py"

#pid = subprocess.Popen([app, motion]).pid

light = "/home/pi/Pimoroni/envirophat/examples/light_detect.py"
#pid2 = subprocess.Popen([app, light]).pid

services = []
#services.extend((motion, light))

services.extend((motion, light))
#services.append(light)
print(services)

def get_pid(name):
        child = subprocess.Popen(["pgrep", '-f', name], stdout=subprocess.PIPE, shell=False)
        response = child.communicate()[0]
        return [int(pid) for pid in response.split()]

for i in services:
        filename = i.split("/")[-1]

        try:
                for pid in get_pid(filename):
                        print("Killing process at " + str(pid))
                        os.kill(pid, signal.SIGTERM)
        except Exception as e:
                print(e)
#services.append(light)
#print(services)
env = os.environ
for i in services:
	print("Starting " + i)
	pid = subprocess.Popen([app, i], env=env, shell=False).pid

