import json
import re
from io import StringIO

def show_dic(dic):
	for k, v in dic.items():
		print(k, ':', v)

# 20

print("# 20")

eng = ""

with open("jawiki-country.json") as f:
	for line in f:
		eng = json.load(StringIO(line))
		if eng["title"] == "イギリス":
			break

text = eng["text"]

print(text)


# 21

print("# 21")

m = text.split('\n')

c = re.compile(r'\[\[Category\:.*\]\]')

for l in m:
	if c.match(l):
		print(l)

# 22

print("# 22")

c = re.compile(r'\[\[Category\:(.*)\]\]')

for l in m:
	r = c.match(l)
	if r:
		print(r.group(1))


# 23

print("# 23")

c = re.compile(r'=(=+)([^=]+)=(=+)')

for l in m:
	r = c.match(l)
	if r:
		s_name = r.group(2).strip()
		s_depth = len(r.group(1))
		print(s_name, ":", str(s_depth))


# 24

print("# 24")

c = re.compile(r'(ファイル|File)\:(.+?)\|')

for l in m:
	r = c.match(l)
	if r:
		print(r.group(2))


# 25

print("# 25")

c = re.compile(r'^\|(.+) = (.+)$')

dic = {}

for l in m:
	r = c.match(l)
	if r:
		dic[r.group(1)] = r.group(2)

print(dic)


# 26

print("# 26")

dic2 = {}

for k, v in dic.items():
	dic2[k] = re.sub(r"\'\'\'\'|\'\'\'|\'\'", "", v)

print(dic2)


# 27

print("# 27")

dic3 = {}

for k, v in dic2.items():
	dic3[k] = re.sub(r"\[\[([^\|\]]+)\]\]", lambda m:m.group(1), v)
	dic3[k] = re.sub(r'\[\[[^\|\]]+\|([^\|\]]+)\]\]', lambda m:m.group(1), dic3[k])

show_dic(dic3)


# 28

print("# 28")

dic4 = {}

for k, v in dic3.items():
	dic4[k] = re.sub(r"<(\S+)\s?.*?>.+?</\1>","", v)
	dic4[k] = re.sub(r'<\S+(\s\S+)*\s*\/>', '', dic4[k])

show_dic(dic4)


# 29

print("# 29")

import urllib.request
import urllib.parse

query = "https://ja.wikipedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url&titles="

query += urllib.parse.quote("File:" + dic4['国旗画像'])

print(query)

data = 0

with urllib.request.urlopen(query) as connection:
   data = connection.read()
   data = json.loads(data)

url = data['query']['pages']['-1']['imageinfo'][0]['url']

urllib.request.urlretrieve(url, dic4['国旗画像'])








