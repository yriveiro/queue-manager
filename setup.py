#-*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="queue-manager",
    version="0.1",
    description="A custom BaseManager to share a queue between processes.",
    author="Yago Riveiro",
    author_email="yago.riveiro@gmail.com",
    url="https://github.com/yriveiro/queue-manager.git",
    packages=["qmanager"]
)
