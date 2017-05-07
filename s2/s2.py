# preparation

import urllib.request
import os
import subprocess

url = "http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt"
title = os.path.basename(url)
urllib.request.urlretrieve(url, "{}".format(title))

def show_file(s):
	with open(s) as f:
		print(f.read())



# 10

print("# 10")

lien_num = 0

with open(title) as f:
	for line in f:
		lien_num += 1

print(lien_num)

com = "wc {}".format(title)
subprocess.run(com.split(" "))


# 11

print("# 11")

with open(title) as f1:
	with open("11" + title, mode="w") as f2:
		for line in f1:
			f2.write(line.replace("\t", " "))

show_file("11" + title)

com1 = ["sed", "-e", "s/\t/ /g", "{}".format(title)]
subprocess.run(com1)

#com2 = ["cat", "{}".format(title), "|", "tr", "\t", " "]
#subprocess.run(com2)

com3 = "expand -t 1 {}".format(title)
subprocess.run(com3.split(" "))


# 12

print("# 12")

with open(title) as f1:
	with open("col1.txt", "w") as f2:
		with open("col2.txt", "w") as f3:
			for line in f1:
				sp = line.split("\t")
				f2.write(sp[0] + "\n")
				f3.write(sp[1] + "\n")

show_file("col1.txt")

show_file("col2.txt")

com1 = ["cut", "-f1", "{}".format(title)]
subprocess.run(com1)

com2 = ["cut", "-f2", "{}".format(title)]
subprocess.run(com2)


# 13

print("# 13")

with open("col1.txt") as f1:
	with open("col2.txt") as f2:
		with open("marged.txt", "w") as f3:
			for l1, l2 in zip(f1,f2):
				f3.write(l1.strip() + "\t" + l2)

show_file("marged.txt")

com = ["paste", "col1.txt", "col2.txt"]
subprocess.run(com)


# 14

print("# 14")

import sys

N = int(sys.argv[1])

with open(title) as f:
	for i in range(0, N):
		print(f.readline(), end="")

print()

com = ["head", "-n", str(N), "{}".format(title)]
subprocess.run(com)


# 15

print("# 15")

s = ""
with open(title) as f:
	s = f.read()

s = s.split("\n")
n = len(s)

for i in range(n - N, n):
	print(s[i])

com = ["tail", "-n", str(N), "{}".format(title)]
subprocess.run(com)


# 16

print("# 16")

s = ""
with open(title) as f:
	s = f.read()

s = s.split("\n")
n = len(s)

import math

for i in range(0, math.ceil(n / N)):
	with open(str(i) + ".txt", mode="w") as f:
		for j in range(i * N, min((i + 1) * N, n)):
			f.write(s[j] + "\n")

for i in range(0, math.ceil(n / N)):
	file_name = str(i) + ".txt"
	print(file_name + "---------")
	show_file(file_name)

com = ["split", "-n", str(N), "{}".format(title)]
subprocess.run(com)


# 17

print("# 17")

s = ""

with open(title) as f:
	s = f.readline().strip()

s = set(s)
print("".join(s))

#com = []
#subprocess.run()


#18

print("# 18")

arr = []

with open(title) as f:
	for line in f:
		arr.append(line.split("\t"))

arr.sort(key=lambda x: x[2])

for i in range(0, len(arr)):
	print("\t".join(arr[i]), end="")

com = ["sort", "", "{}".format(title)]


# 19

print("# 19")

import operator

dic = {}

with open(title) as f:
	for line in f:
		key = line.split("\t")[0]
		dic[key] = dic.get(key, 0) + 1

dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)

for item in dic:
	print("\t".join([str(item[1]), item[0]]))
























