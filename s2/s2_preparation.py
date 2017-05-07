# s2 preparation

import urllib.request
import os

url = "http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt"
title = os.path.basename(url)
urllib.request.urlretrieve(url, title)