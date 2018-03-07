import requests
from lxml import etree

def requests_view(response):
    import webbrowser
    request_url = response.url
    base_url = '<head><base href="%s">'%(request_url)
    base_url = base_url.encode()
    content = response.content.replace(b"<head>",base_url)
    tem_html = open('tmp.html','wb')
    tem_html.write(content)
    tem_html.close()
    webbrowser.open_new_tab("tmp.html")

response = requests.get("http://bj.ganji.com/fang1/01/")
#requests_view(response)
html = etree.HTML(response.content.decode())
items = html.xpath(".//div[@class='f-list js-tips-list']/div[@class='f-list-item ershoufang-list']")
len(items)
#for i in items:
 #   print(i.xpath(".//dd[@class='dd-item title'/a/text()]"))