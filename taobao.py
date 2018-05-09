# coding=utf-8

import sys
import subprocess

keywords = sys.argv[1:]

url = "https://s.taobao.com/"
for i in keywords:
	url += i + "+"
url = url[:-1] 
subprocess.call(["open",url])

