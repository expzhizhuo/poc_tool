"""
@Project ：pocsuite3测试文件
@File    ：Tools.py
@IDE     ：PyCharm
@Author  ：zhizhuo
@Date    ：2023/7/25 15:11
"""

import json
import random
import socket
import struct
from urllib.parse import urlparse, quote, unquote
import base64
import string

UA = '''
Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.65
Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.65
Mozilla/5.0 (Windows NT 5.1; U; zh-cn; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50
Mozilla/5.0 (Windows NT 5.1; U; zh-cn; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.53
Mozilla/5.0 (Windows NT 5.1; U; zh-cn; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.70
Opera/8.50 (Windows NT 4.0; U; zh-cn)
Opera/8.54 (Windows NT 4.0; U; zh-cn)
Opera/9.02 (Windows NT 5.1; U; zh-cn)
Opera/9.23 (Windows NT 5.1; U; zh-cn)
Opera/9.25 (Windows NT 5.1; U; zh-cn)
Opera/9.26 (Windows NT 5.1; U; zh-cn)
Opera/9.61 (Windows NT 5.1; U; zh-cn) Presto/2.1.1
Opera/9.62 (Windows NT 5.1; U; zh-cn) Presto/2.1.1
Opera/9.64 (Windows NT 6.0; U; zh-cn) Presto/2.1.1
Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.2.15 Version/10.00
Opera/9.80 (Windows NT 5.2; U; zh-cn) Presto/2.6.30 Version/10.63
Opera/9.80 (Windows NT 6.0; U; zh-cn) Presto/2.5.22 Version/10.50
Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.2.15 Version/10.00
Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.5.22 Version/10.50
Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.30 Version/10.61
Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.37 Version/11.00
Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.7.62 Version/11.01
Opera/10.60 (Windows NT 5.1; U; zh-cn) Presto/2.6.30 Version/10.60
Mozilla/5.0 (Windows NT 5.1; U; zh-cn; rv:1.8.1) Gecko/20091102 Firefox/3.5.5
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.0.9) Gecko/20061206 Firefox/1.5.0.9
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.16) Gecko/20080702 Firefox/2.0.0.17
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.18) Gecko/20081029 Firefox/2.0.0.18
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.9) Gecko/20071025 Firefox/2.0.0.9
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1b4) Gecko/20090423 Firefox/3.5b4
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1b4) Gecko/20090423 Firefox/3.5b4 (.NET CLR 3.5.30729)
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.4) Gecko/20100503 Firefox/3.6.4 (.NET CLR 3.5.30729)
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.4) Gecko/20100513 Firefox/3.6.4 (.NET CLR 3.5.30729)
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b3) Gecko/2008020514 Firefox/3.0b3
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030714 Firefox/3.0b4
Mozilla/5.0 (Windows; U; Windows NT 5.2; zh-CN; rv:1.9.1.5) Gecko/Firefox/3.5.5
Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.19
Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.9.0.19) Gecko/2010031422 Firefox/3.0.19 (.NET CLR 3.5.30729)
Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.9.2.4) Gecko/20100513 Firefox/3.6.4
Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.9.2.6) Gecko/20100625 Firefox/3.6.6 GTB7.1
Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 (.NET CLR 3.5.30729)
Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3
Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12 (.NET CLR 3.5.30729; .NET4.0E)
Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.14) Gecko/20110218 Firefox/3.6.14
Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)
Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8
Mozilla/5.0 (X11; U; Linux i686; zh-CN; rv:1.9.1.6) Gecko/20091216 Fedora/3.5.6-1.fc11 Firefox/3.5.6 GTB6
Mozilla/5.0 (X11; U; Linux i686; zh-CN; rv:1.9.1.8) Gecko/20100216 Fedora/3.5.8-1.fc12 Firefox/3.5.8
Mozilla/5.0 (X11; U; Linux i686; zh-CN; rv:1.9.2.8) Gecko/20100722 Ubuntu/10.04 (lucid) Firefox/3.6.8
Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-cn) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; zh-cn) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27
Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16
Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1
Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/533+ (KHTML, like Gecko)
'''


class Tools:
    def __init__(self):

        self._ua_list = [u for u in UA.split('\n') if u]

    def get_random_ua(self):
        """
        获取随机的ua头
        """
        return self._ua_list[random.randint(0, len(self._ua_list) - 1)]

    @staticmethod
    def get_random_str(len: int = 1) -> str:
        """
        生成指定长度的随机字符串，默认长度是1
        """
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(len))

    @staticmethod
    def get_random_num(len: int = 1) -> int:
        """
        生成指定长度的随机数字，默认长度是1
        """
        return random.randint(10 ** (len - 1), (10 ** len) - 1)

    @staticmethod
    def get_random_ip():
        """
        生成随机ip地址
        """
        ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        return ip

    @staticmethod
    def url_encode(url_string):
        """
        只针对特殊字符进行url编码
        """
        return quote(url_string)

    @staticmethod
    def url_encode_all(url_string, num: int = 1) -> str:
        """
        全url编码，num编码次数
        """
        encode_string = ""
        for _ in range(num):
            encode_string = "".join(hex(ord(char)).replace("0x", "%") for char in url_string)
            url_string = encode_string
        return encode_string

    @staticmethod
    def url_decode(url_string, num: int = 1):
        """
        url编码解密
        """
        str_decode = url_string
        for _ in range(num):
            str_decode = unquote(str_decode)
        return str_decode

    @staticmethod
    def get_http_version(res):
        """
        获取相应或者请求的HTTP协议的版本信息
        """
        if res.raw.version == 20:
            version = "HTTP/2.0"
        else:
            version = "HTTP/1.1"
        return version

    def get_req(self, res):
        """
        获取请求信息，拼接生成请求数据包
        """
        try:
            if res.request.body is not None:
                if type(res.request.body) == bytes:
                    # 转换成utf-8 编码，如果不能解码的直接略过
                    body = res.request.body.decode('utf-8', 'ignore')
                elif type(res.request.body) == dict:
                    body = json.dumps(res.request.body)
                else:
                    body = res.request.body
            else:
                body = ''
            req = self.get_req_header(res) + body
        except Exception:
            req = None
        return req

    def get_req_header(self, res):
        """
        获取请求头
        :param res:
        :return:
        """
        try:
            host = urlparse(res.url).netloc
            headers = ''.join(header + '\n' for header in ["{}: {}".format(
                key, res.request.headers[key]) for key in res.request.headers.keys()])
            req = f"{res.request.method} {res.request.path_url} {self.get_http_version(res)}\nHost: {host}\n{headers}\n"
        except Exception:
            req = None
        return req

    def get_res(self, res):
        """
        获取响应信息，拼接请求数据包
        """
        try:
            response = self.get_res_header(res) + res.text
        except Exception:
            response = None
        return response

    def get_res_header(self, res):
        """
        获取响应头
        :param res:
        :return:
        """
        try:
            res.encoding = res.apparent_encoding
            res_headers = ''
            for key in res.headers:
                res_headers += key + ': ' + res.headers[key] + '\n'
            response = f"{self.get_http_version(res)} {res.status_code} {res.reason}\n{res_headers}\n"
        except Exception:
            response = None
        return response

    @staticmethod
    def base64_encode(data):
        """
        base64编码
        """
        base64_endata = base64.b64encode(str(data).encode()).decode()
        return base64_endata

    @staticmethod
    def base64_decode(data):
        """
        base64解密
        """
        base64_dedata = base64.b64decode(str(data)).decode()
        return base64_dedata

    def get_all_requests(self, res):
        """
        获取原始请求数据包，相应数据包
        :param res:object
        :return:对象{}
        """
        return {"request": self.get_req(res), "response": self.get_res(res)}


tools = Tools()
