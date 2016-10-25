import searchengine
'''
crawler = searchengine.crawler('searchindex.db')
#crawler.createindextables()
pages = ['http://www.jetbrains.com/pycharm/download/#section=windows']
crawler.crawl(pages)
'''

#import urllib2
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin

page = 'http://www.51testing.com/html/39/n-860239.html'
c = urllib.request.urlopen(page)
cr = c.read()
soup = BeautifulSoup(cr,'html.parser')
c = soup.contents ##得到所有tag，方便以后分析

links=soup('a')
[print(link) for link in links]
for link in links:
    if ('href' in dict(link.attrs)):
        url = urljoin(page, link['href'])
    if url.find("'") != -1: continue
    url = url.split('#')[0]  # remove location portion
    #if url[0:4] == 'http' and not self.isindexed(url):
    #    newpages[url] = 1
    #linkText = self.gettextonly(link)

'''
c = soup.contents[0] ##返回html文件内的第一个tag
print(type[c])
print (c)

c = soup.contents[1] ##返回的是第一个tag后面的换行符
print (type[c])
print (c,'utf-8')

c = soup.contents[2] ##返回的是<html xmlns...></html>节点
print (type(c))
print (c)

c = soup.contents
print (type(c[2].contents[1]))##注意换行符也是子节点
print (c[2].contents[1])
'''