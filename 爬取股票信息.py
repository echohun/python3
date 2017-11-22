import re
import requests
from bs4 import BeautifulSoup
import traceback

def gethtmltext(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getstocklist(east_url, infolist):
    east_source = gethtmltext(east_url)
    soup = BeautifulSoup(east_source, "html.parser")
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            retext = re.compile(r's[hz]\d{6}')
            infolist.append(re.findall(retext,href)[0])
        except:
            continue

def getstockinfo(baidu_url, infolist, out_file):
    count = 0
    for i in infolist:
        url = baidu_url + i + ".html"
        baidu_source = gethtmltext(url)
        try:
            if baidu_source == "":
                continue
            dic = {}
            soup =BeautifulSoup(baidu_source,"html.parser")
            stockinfo = soup.find('div',attrs={'class':"stock-bets"})
            name = stockinfo.find_all(attrs={'class': 'bets-name'})[0]
            dic.update({'股票名称': name.text.split()[0]})
            keylist =stockinfo.find_all('dt')
            valuelist = stockinfo.find_all('dd')
            for i in range(len(keylist)):
                key = keylist[i].text
                val = valuelist[i].text
                dic[key] = val

            with open(out_file, 'a', encoding='utf-8') as f:
                f.write(str(dic) + '\n')
                count = count +1
                print("\r当前进度: {:.2f}%".format(count * 100 / len(infolist)), end="")
        except:
            count = count + 1
            print("\r当前进度: {:.2f}%".format(count * 100 / len(infolist)), end="")
            #traceback.print_exc()   #返回错误信息（调试用）
            continue

def main():
    east_url = "http://quote.eastmoney.com/stocklist.html"      #东方财富网
    baidu_url = "https://gupiao.baidu.com/stock/"           #百度股票
    infolist = []                                       #存放信息
    output_file = 'H:/BaiduStockInfo.txt'       #存储爬取信息的位置
    getstocklist(east_url, infolist)                #抓取证券代码
    getstockinfo(baidu_url, infolist, output_file)  #抓取证券详细信息并保存在txt中

main()

