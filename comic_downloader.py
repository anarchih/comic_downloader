from bs4 import BeautifulSoup
import urllib.request
import shutil
url = ""
input(url)
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
#entire_url = furl[dm-1]+k[1]
class MyOpener(urllib.request.FancyURLopener):
	version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
myopener = MyOpener()
file_name = "comic"
entire_name = ""
<<<<<<< HEAD
folder_name =""
input(folder_name)
os.system("mkdir "+folder_name)
=======
>>>>>>> parent of 60d27e0... make a folder for downloaded comic
for i in range (0,len(k)):
	entire_url = furl[dm-1] + k[i]
	entire_name = file_name + str(i+1) + ".jpg"
	myopener.retrieve(entire_url,"./" + folder_name + "/" + entire_name)
#myopener = MyOpener()
#myopener.retrieve(entire_url, file_name)
