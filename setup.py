import io
import os

from setuptools import setup, find_packages

current_dir = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(current_dir, "README.md"), encoding="utf-8") as fd:
    desc = fd.read()

setup(
    name="poc_tool",
    license='MIT',
    version="1.2.1",
    long_description=desc,
    long_description_content_type="text/markdown",
    description="Python Poc 还原原始http请求数据包以及常用工具集成化封装类，可以更快帮助您完成POC的书写及调试",
    author="zhizhuo",
    author_email="zhizhuoshuma@163.com",
    url='https://github.com/zhizhuoshuma/poc_tool',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "colorama"
    ],
    python_requires=">=3.7",
)
