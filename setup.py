import os
from setuptools import setup, find_packages

setup(
    name="poc_tool",
    license='MIT',
    version="1.0.5",
    description="python Poc 还原原始http请求数据包以及常用工具集成化封装",
    author="zhizhuo",
    author_email="zhizhuoshuma@163.com",
    url='https://github.com/zhizhuoshuma/poc-tool',
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    python_requires=">=3.8",
)
