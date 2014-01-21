from bs4 import BeautifulSoup
import urllib.request
import shutil
url = "http://mh.99770.cc/comic/2779/21390/"
fp = urllib.request.urlopen(url)
org_bytes = fp.read()
org_str = org_bytes.decode("utf-8",'ignore')
soup = BeautifulSoup(''.join(org_str))
tag = soup.find('script').string
l = list (tag)
#print (l[0])
#l = ['a','b','c','d','/','a','|','b','|','c']
k = []
#l = l[1:]
#print (l[0], l[1])
string = ''
for i in l:
#	l = l[1:]
#	print (l[0])
	if l[0] == "/":
		string = ''.join(l) 
		k = string.split("|")
		break;
	l = l[1:]
print (k)
