"""
@Project ：pack 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：zhizhuo
@Date    ：2024/3/1 13:16 
"""
from poc_tool import tools


def main():
    url = "http://127.0.0.1:80/"
    url = "http://2408:823c:4b8d:424:20c:29ff:fecd:205b:8080"
    url = "http://2408:823c:4b8d:424:20c:29ff:fecd:205b"
    url = "http://2408:823c:4b8d:424:20c:29ff:fecd:205b:8080/123"
    # url = "http://127.0.0.1:9090/ouhjkh"
    # url = "http://www.baidu.com:443"
    # url = "127.0.0.1"
    res = tools.get_url_format(url=url)
    print(res)


if __name__ == '__main__':
    main()
