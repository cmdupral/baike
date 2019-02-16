class HtmlOutputer(object):
    def __init__(self):
        self.datas = []   # 类里面的全局变量，先存一个数据备份，供output等函数使用

    def collect_data(self, new_url, new_data):
        assert new_url is not None
        assert new_data is not None

        self.datas.append((new_url, new_data))

    def output_html(self):
        """
        输出到output.html
        :return:
        """
        file = open('output.html', mode='w')

        file.write("<html>")
        file.write("<body>")

        for row in self.datas:
            file.write("<tr>")
            file.write(f"链接:<td>{row[0]}</td><br>")
            file.write(f"标题:<td>{row[1]}{'title'}</td><br>")
            file.write(f"简介:<td>{row[1]}{'summary'}</td><br>")

            file.write("</tr>")
        file.write("</body>")
        file.write("</html>")

    def save_db(self):
        """
        保存到数据库
        :return:
        """
        pass
