# 下载器
import requests


class HtmlDownloader(object):
    def download(self, url):
        assert url is not None, "download()方法参数url不能为None"

        # if url is None:
        #     raise Exception("参数url不能为None")
        #
        # if url is None:
        #     return  None

        headers = {
            'Host': 'baike.baidu.com',
            'referer': 'https://baike.baidu.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception('请求失败， code {response.status_code}')

        return response.content.decode(encoding='utf-8')
