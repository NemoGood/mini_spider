#encoding:UTF-8

from bs4 import BeautifulSoup
import urllib
import urllib2

class HtmlParser:

    def getAllLink(self,url):
        htmlPage = urllib2.urlopen(url).read()
        soup = BeautifulSoup(htmlPage)
        for tmp in soup.find_all("a"):
            print tmp.get('href')

    def getAllImg(self,url):
        htmlPage = urllib2.urlopen(url).read()
        soup = BeautifulSoup(htmlPage)
        for tmp in soup.find_all("img"):
            print tmp.get('src')


if __name__=="__main__":
    htmlParser = HtmlParser()
    htmlParser.getAllImg("http://www.baidu.com")