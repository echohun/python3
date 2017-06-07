import requests
import re
url = 'http://210.27.8.14/login'
hea = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
       'Accept-Encoding':'gzip, deflate',
        'Referer':'http://210.27.8.14',
        'Content-Type':'application/x-www-form-urlencoded'
       }
data = {'username': 'xxxxxx',
	'password': 'xxxxxx'
	}
s = requests.session()
r = s.post(url,data=data,headers=hea)
cookies = r.cookies
r = s.get('http://210.27.8.14/runner/',headers=hea,cookies=cookies)
print r
l = r.text
#print l
dd = r"td>(\d\d)</td"    #只输出括号里面的，如果不知道数的位数用\d*
d = re.compile(dd)
relist = re.findall(d,l)
for cishu in relist:
    print cishu
