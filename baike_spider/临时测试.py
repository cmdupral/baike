from html_downloader import HtmlDownloader

downloader = HtmlDownloader()
html_content = downloader.download(url='https://baike.baidu.com/item/Python/407313')
print(html_content)