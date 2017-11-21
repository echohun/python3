import re
import requests

def gethtmltext(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def parsepage(ilt, html):
    try:
        reprice = re.compile(r'\"view_price\"\:\"[\d\.]*\"')
        retitle = re.compile(r'\"raw_title\"\:\".*?\"')
        plt = re.findall(reprice, html)
        tlt = re.findall(retitle, html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")
def printgoodslist(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods = 'u盘'        #商品名称
    depth = 3            #爬取页数
    starturl = 'https://s.taobao.com/search?q=' + goods     #起始地点
    infolist = []                                           #结果
    for i in range(depth):
        try:
            url = starturl + '&s=' + str(44 * i)
            html = gethtmltext(url)
            parsepage(infolist, html)
        except:
            continue
    printgoodslist(infolist)


main()
