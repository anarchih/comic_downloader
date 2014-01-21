from bs4 import BeautifulSoup
import urllib.request
import shutil
url = "http://mh.99770.cc/comic/2779/21390/"
fp = urllib.request.urlopen(url)
org_bytes = fp.read()
org_str = org_bytes.decode("utf-8",'ignore')
soup = BeautifulSoup(''.join(org_str))
tag = soup.find('script').string
print (tag)
