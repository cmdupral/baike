from lxml import etree
class HtmlParser(object):
    def parse(self, html_content):
        """# 接受网页的HTML响应，解析，获取想要的数据

        :param html_content:<html></html>
        :return: new_urls
        :return:new_data
        """
        assert html_content is not None, "html_content为空 请检查"

        dom = etree.HTML(html_content)

        pattern_title = '//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()'

        pattern_summary = '//div[@class="lemma-summary"]/div/text()'
        pattern_href = '//div[@class="main-content"]//a[@target="_blank"]/@href'

        title = dom.xpath(pattern_title)
        summary = dom.xpath(pattern_summary)
        new_urls = dom.xpath(pattern_href)

        for index, href in enumerate(pattern_href):
            # todo 判断链接是否合法，可以用正则或str.find('item')
            new_urls[index] = 'https://baike.baidu.com'+href

        # return title, summary, new_urls
        # context = {}
        # context{'title'} = title
        # context{'summary'} = summary
        # context{'new_urls'} = new_urls
        new_data = {'title': title, 'summary': summary}
        return new_urls, new_data

