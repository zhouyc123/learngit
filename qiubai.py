import requests
from lxml import etree
from time import sleep

def down_pic(imgs):
    file_dir = "E:/pic/{}"
    for i in imgs:
        file_name = i.split("/")[-1]
        file_content = requests.get(i)
        if file_content.status_code != 200:
            print(i,file_content.status_code)
        else:
            try:
                with open(file_dir.format(file_name),'wb') as f:
                    f.write(file_content.content)
            except:
                print(file_name)


def all_links(url):
    if '8.html' in url:
        print(url)
        return 0
    response = requests.get(url)
    html = etree.HTML(response.content)

    imgs = html.xpath(".//div[@id='wrapper']//div[@class='ui-module']//img/@src")
    down_pic(imgs)

    links = html.xpath(".//div[@class='page']//a[contains(text(),'下一页')]/@href")
    if len(links)<1:
        pass
    else:
        sleep(0.1)
        host = "http://www.qiubaichengren.net/"
        all_links(host+links[0])


all_links("http://www.qiubaichengren.net/")

