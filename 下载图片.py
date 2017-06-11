import requests
import re
import urllib

url=("http://www.uuzdaisuki.com")

hea={
        'User-Agent':   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
        'Accept':   'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Content-Type':'application/x-www-form-urlencoded'
       }

r = requests.get(url,headers=hea)
print r
l = r.text
dd = r"<img src=\"(.*?)\" alt="                                                             #只输出括号里面的
d = re.compile(dd)
relist = re.findall(d,l)
x=1
for img in relist:
    print img
    urllib.urlretrieve(img,'%s.png' % x)
    x+=1
