# s2_template

import subprocess

def show_file(s):
	print("----file----")
	print("show: " + s)
	with open(s) as f:
		print(f.read())

def exec_command(com):
	print("----command----")
	print("exec: " + com)
	subprocess.run(com, shell=True)


title = "hightemp.txt"
