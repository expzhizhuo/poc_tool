# 一个方便安全测试人员书写poc的工具库集合

## 描述

避免重复造轮子以及代码的简洁，将常用的方法集成化封装到一起，提高代码的整洁和便携。

## 安装

```shell
pip install poc-tool
```

## 使用

### 工具类tools使用

```shell
from poc_tool import tools

# 获取请求和响应数据包，传入response
tools.get_all_requests()

# 获取请求头，传入response
tools.get_req_header()

# 获取请求数据包，传入response
tools.get_req()

# 获取响应头，传入response
tools.get_res_header()

# 获取响应数据包，传入response
tools.get_res()

# 获取http请求版本，传入response
tools.get_http_version()

# 获取随机ua头
tools.get_random_ua()

# 获取随机ip地址
tools.get_random_ip()

# 获取随机数据，传入number类型长度
tools.get_random_num()

# 获取随机字符串，传入number类型长度
tools.get_random_str()

# base64加密，传入字符串
tools.base64_encode()

# base64解密，传入加密字符串
tools.base64_decode()

# url编码，传入字符串
tools.url_encode()

# url解码，传入url编码字符串
tools.url_decode()

# url全编码，传入字符串
tools.url_encode_all()

# url地址格式化，传入url或者IP地址，例如：'127.0.0.1:8988'，‘https://127.0.0.1:8899/api/v1’
tools.get_url_format()

# 验证是否是ip
tools.tools.verify_ip()

# 验证是否是ipv4 ip
tools.tools.verify_ipv4()

# 验证是否是ipv6 ip
tools.tools.verify_ipv6()
```

### 日志输出类logger使用

默认日志输出是INFO模式，如果需要所有信息都输出请设置成DEBUG模式

```shell
from poc_tool.log import log, LoggingLevel, LOGGER

# 设置日志等级，可以设置info，error，debug，warning，success
LOGGER.setLevel(LoggingLevel.INFO)

# 使用
log.info("zhizhuo")
log.success("zhizhuo")
log.error("zhizhuo")
log.warning("zhizhuo")
log.debug("zhizhuo")
```

### 文件hex编码查看，类似于Linux中的xxd命令

```python
from poc_tool import hex_dump


# 或者使用 from poc_tool.tools import hex_dump引入
# 参数说明，file_path文件路径，bytes_per_line每行的字节大小，默认是16
# lines获取多少行数据，默认是全部，可以自己定义传入

def hex_test():
    hex_data = hex_dump(file_path="../poc编写规则.zip", lines=10)
    print(hex_data)
```