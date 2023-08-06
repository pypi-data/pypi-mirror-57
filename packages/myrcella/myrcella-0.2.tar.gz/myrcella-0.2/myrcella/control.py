import subprocess
from .__init__ import name
from doreah.control import mainfunction
from doreah.io import col
import os
import signal

PROCESS_NAME = "Myrcella"
PACKAGE_NAME = name
PRETTY_NAME = "Myrcella"



def getInstance():
	try:
		output = subprocess.check_output(["pidof",PROCESS_NAME])
		pid = int(output)
		return pid
	except:
		return None

def is_running():
	return getInstance() is not None


def start():
	try:
		p = subprocess.Popen(["python3","-m",PACKAGE_NAME + ".main"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
		print(col["green"](PRETTY_NAME + " started!") + " PID: " + str(p.pid))
	except:
		print("Error while starting " + PRETTY_NAME + ".")
		return False

def restart():
	wasrunning = stop()
	start()
	return wasrunning

def stop():
	pid = getInstance()
	if pid is None:
		print("Server is not running")
		return False
	else:
		os.kill(pid,signal.SIGTERM)
		print(PRETTY_NAME + " stopped! PID: " + str(pid))
		return True


actions = {
	"start":start,
	"restart":restart,
	"stop":stop
}

@mainfunction({},shield=True)
def main(cmd,*args,**kwargs):
	if cmd in actions: actions[cmd](*args,**kwargs)
	else: print("Valid commands: " + " ".join(a for a in actions))
