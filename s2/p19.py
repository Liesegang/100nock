# 19

print("# 19")

import collections
import operator
import s2_lib as s2

r = collections.Counter()

with open(s2.title) as source:
	for line in source:
		r.update([line.split("\t")[0]])

r = r.most_common()

for item in r:
	print("\t".join([str(item[1]), item[0]]))

com = "cut -f1 {} | sort | uniq -c | sort -k1,1 -r".format(s2.title)
s2.exec_command(com)