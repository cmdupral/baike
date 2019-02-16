# url 调度管理器
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 待爬取
        self.old_urls = set()  # 爬取过的

    def add_new_url(self, url):
        """
        添加一个新链接
        :param url:
        :return:
        """
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        """
        还没有待爬取的url
        :return:
        """
        if len(self.new_urls) > 0:
            return True
        else:
            return False

    def get_new_url(self):
        """
        取出一个新的url准备请求它
        :return:
        """
        new_url = self.new_urls.pop()  # set.pop()随机删除一个元素并返回
        self.old_urls.add(new_url)
        return new_url

    def add_new_urls(self, urls):
        """
        一个词条的上所有连接添加self.new_urls中
        :param urls:['列表']
        :return:
        """
        assert urls is not None, "urs不能为空"
        for url in urls:
            self.new_urls.add(url)
