"""
@Project ：pocsuite3测试文件
@File    ：Tools.py
@IDE     ：PyCharm
@Author  ：zhizhuo
@Date    ：2023/7/25 15:11
"""
import base64
import json
import random
import re
import socket
import string
import struct
from urllib.parse import urlparse, quote, unquote
import requests.models
from fake_useragent import UserAgent


class Tools:

    def get_url_format(self, url: str) -> str:
        """
        url格式化，格式成http(s)://example.com
        :param url: IP地址
        :return: url格式化地址
        """
        url = url.rstrip("/") + "/"
        url = f"http://{url}" if not url.startswith(('http://', 'https://')) else url
        domain_match = re.search('://(.*?)/', url)
        if domain_match:
            domain = domain_match.group(1)
            port = domain.split(':')[-1]
            domain_without_port = domain.replace(f':{port}', '')
            if 0 < len(port) < 6 and self.verify_ipv6(domain_without_port):
                domain = f"[{domain_without_port}]:{port}"
            elif self.verify_ipv6(domain):
                domain = f"[{domain}]"
            protocol = 'http' if port != '443' else 'https'
            domain_part = domain_without_port if port in ('80', '443') else domain
            url = f"{protocol}://{domain_part}"
        return url

    def verify_ip(self, ip: str) -> bool:
        """
        验证是否是ip地址
        :param ip:ip
        :return:True or False
        """
        if self.verify_ipv4(ip) or self.verify_ipv6(ip):
            return True
        return False

    @staticmethod
    def verify_ipv4(ip: str) -> bool:
        """
        验证是否是ipv4地址
        :param ip:ip
        :return:True or False
        """
        try:
            socket.inet_pton(socket.AF_INET, ip)
        except socket.error:
            return False
        return True

    @staticmethod
    def verify_ipv6(ip: str) -> bool:
        """
        验证是否是ipv6地址
        :param ip:ip
        :return:True or False
        """
        try:
            socket.inet_pton(socket.AF_INET6, ip)
        except socket.error:
            return False
        return True

    @staticmethod
    def get_random_ua() -> str:
        """
        获取随机的ua头
        :return: 随机ua头
        """
        ua = UserAgent()
        return ua.random

    @staticmethod
    def get_random_str(len: int = 1) -> str:
        """
        生成指定长度的随机字符串，默认长度是1
        :param len: 生成字符串长度
        :return: 随机字符串
        """
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(len))

    @staticmethod
    def get_random_num(len: int = 1) -> int:
        """
        生成指定长度的随机数字，默认长度是1
        :param len: 生成随机数字长度
        :return: 随机数字
        """
        return random.randint(10 ** (len - 1), (10 ** len) - 1)

    @staticmethod
    def get_random_str_num(len: int = 1) -> str:
        """
        生成指定长度的随机字母和数字混合字符串，默认长度是1
        :param len: 生成字符串长度
        :return: 随机混合字符串
        """
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(len))

    @staticmethod
    def get_random_ip() -> str:
        """
        生成随机ip地址
        :return: ip地址
        """
        ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        return ip

    @staticmethod
    def url_encode(url_string: str) -> str:
        """
        只针对特殊字符进行url编码
        :param url_string: 待url编码数据
        :return: url编码后的字符串
        """
        return quote(url_string)

    @staticmethod
    def url_encode_all(url_string: str, num: int = 1) -> str:
        """
        全url编码，num编码次数
        :param url_string: 待url编码数据
        :param num: 编码次数
        :return: url编码后的字符串
        """
        encode_string = ""
        for _ in range(num):
            encode_string = "".join(hex(ord(char)).replace("0x", "%") for char in url_string)
            url_string = encode_string
        return encode_string

    @staticmethod
    def url_decode(url_string: str, num: int = 1) -> str:
        """
        url编码解密
        :param url_string: 待url解密数据
        :param num: 需要url解密次数
        :return: url解密结果
        """
        str_decode = url_string
        for _ in range(num):
            str_decode = unquote(str_decode)
        return str_decode

    @staticmethod
    def get_http_version(res: requests.models.Response) -> str:
        """
        获取相应或者请求的HTTP协议的版本信息
        :param res: 请求响应对象
        :return: HTTP协议版本
        """
        if res.raw.version == 20:
            version = "HTTP/2.0"
        else:
            version = "HTTP/1.1"
        return version

    def get_req(self, res: requests.models.Response) -> str:
        """
        获取请求数据包
        :param res: 请求响应对象Response
        :return: 请求数据包
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

    def get_req_header(self, res: requests.models.Response) -> str:
        """
        获取请求头
        :param res: 请求响应对象Response
        :return: 请求头
        """
        try:
            host = urlparse(res.url).netloc
            headers = ''.join(header + '\n' for header in ["{}: {}".format(
                key, res.request.headers[key]) for key in res.request.headers.keys()])
            req = f"{res.request.method} {res.request.path_url} {self.get_http_version(res)}\nHost: {host}\n{headers}\n"
        except Exception:
            req = None
        return req

    def get_res(self, res: requests.models.Response) -> str:
        """
        获取响应数据包
        :param res: 请求响应对象Response
        :return: 响应数据包
        """
        try:
            response = self.get_res_header(res) + res.text
        except Exception:
            response = None
        return response

    def get_res_header(self, res: requests.models.Response) -> str:
        """
        获取响应头
        :param res: 请求响应对象Response
        :return: 响应头
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
    def base64_encode(data) -> str:
        """
        base64编码
        :param data: 待base64加密数据
        :return: base64加密数据
        """
        base64_endata = base64.b64encode(str(data).encode()).decode()
        return base64_endata

    @staticmethod
    def base64_decode(data) -> str:
        """
        base64解密
        :param data: 待base64解密数据
        :return: base64解密数据
        """
        base64_dedata = base64.b64decode(str(data)).decode()
        return base64_dedata

    def get_all_requests(self, res: requests.models.Response) -> dict:
        """
        获取原始请求数据包，相应数据包
        :param res: 请求响应对象Response
        :return: 请求数据包和响应数据包
        """
        return {"request": self.get_req(res), "response": self.get_res(res)}


tools = Tools()
