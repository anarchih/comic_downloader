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
dm = 0
furl =  ["http://58.215.241.39:9728/dm01/","http://58.215.241.39:9728/dm02/","http://58.215.241.39:9728/dm03/","http://58.215.241.206:9728/dm04/","http://58.215.241.39:9728/dm05/","http://58.215.241.39:9728/dm06/","http://58.215.241.39:9728/dm07/","http://58.215.241.39:9728/dm08/","http://58.215.241.206:9728/dm09/","http://58.215.241.39:9728/dm10/","http://58.215.241.39:9728/dm11/","http://58.215.241.206:9728/dm12/","http://58.215.241.39:9728/dm13/","http://173.231.57.238/dm14/","http://58.215.241.206:9728/dm15/","http://142.4.34.102/dm16/"]

while True:
	if l[-1].isdigit():
		dm=int(l[-1])
	if l[-1]!='g':
		l = l[:-1]	
	else :
		break;
while True:
#	l = l[1:]
#	print (l[0])
	if l[0] == "/":
		string = ''.join(l) 
		k = string.split("|")
		break;
	l = l[1:]
print (furl[dm-1]+k[0])
