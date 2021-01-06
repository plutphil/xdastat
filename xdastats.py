
#div.node:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > dl:nth-child(2) > dd:nth-child(1)
import requests
import requests_cache
from bs4 import BeautifulSoup
requests_cache.install_cache('demo_cache')
req=requests.get('https://forum.xda-developers.com/all-forums-by-manufacturer')
soup = BeautifulSoup(req.text,'html.parser')

#                  div.node > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(1)
#print(soup.select("div.node > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > dl:nth-child(1) > dd:nth-child(2)"))
#     div.node:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > dl:nth-child(2) > dd:nth-child(2)
def numberparse(s):
    c = s[-1]
    if c in "0123456789.":
        return int(s)
    if c == 'K':
        return int(float(s[:-1])*1000.0)
    if c == 'M':
        return int(float(s[:-1])*1000000.0)
    
    pass
list1=soup.select("div.node > div:nth-child(1) > div:nth-child(2)")
len1 = len(list1)
i1=0
for e in list1:
    e2=e.select("div:nth-child(2) > div:nth-child(1)")[0]
    title=e.select("h3:nth-child(1) > a:nth-child(1)")[0]
    #print(title['href'])
    req=requests.get('https://forum.xda-developers.com'+title['href'])
    soup2 = BeautifulSoup(req.text,'html.parser')
    #div.node:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(1)
    #div.node:nth-child(8) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(1)
    list2=soup2.select("div.node > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(1)")
    len2= len(list2)
    i2=0
    for node in list2:
        #print(node.string)
        #print(node['href'])
        req=requests.get('https://forum.xda-developers.com'+node['href'])
        soup3 = BeautifulSoup(req.text,'html.parser')
        #div.node:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(1)
        #div.node:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > dl:nth-child(1) > dd:nth-child(1)
        #div.node:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > dl:nth-child(1) > dd:nth-child(1)
        #div.node:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > dl:nth-child(1) > dd:nth-child(1)
        #div.node:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > dl:nth-child(2) > dd:nth-child(1)
        #div.node:nth-child(3) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1) > a:nth-child(1)
        for n2 in soup3.select("div.node > div:nth-child(1) > div:nth-child(2)"):
            
            title=n2.select("h3:nth-child(1) > a:nth-child(1)")[0]
            if(title.string.find("ROM")!=-1):
                out=""
                out+=title.string+"\t"
                #out+="\t"+'https://forum.xda-developers.com'+title['href']
                try:
                    e3=n2.select("div:nth-child(3) > div:nth-child(1)")[0]
                    out+=str(numberparse(e3.select("dl:nth-child(1) > dd:nth-child(1)")[0].string))+"\t"
                    out+=str(numberparse(e3.select("dl:nth-child(2) > dd:nth-child(1)")[0].string))+"\t"
                    
                except Exception as ex:
                    #print(ex)
                    #print(n2)
                    #print(out)
                    #exit(-1)
                    pass
                print(out)
        i2+=1
        #print("1:"+str(i1)+"/"+str(len1)+"  "+str(i1*100/len1)+"%")
        #print("2:"+str(i2)+"/"+str(len2)+"  "+str(i2*100/len2)+"%")
    #print(title.string
    #+"\t"+str(numberparse(e2.select("dl:nth-child(1) > dd:nth-child(2)")[0].string))
    #+"\t"+str(numberparse(e2.select("dl:nth-child(2) > dd:nth-child(2)")[0].string)))
    i1+=1

    
    
