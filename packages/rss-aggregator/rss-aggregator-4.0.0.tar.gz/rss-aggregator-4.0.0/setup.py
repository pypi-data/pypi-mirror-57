from setuptools import find_packages
from setuptools import setup

setup(
    name='rss-aggregator',
    version='4.0.0',
    packages=find_packages(),
    author='Vadim Rashkevich',
    author_email='vadimrashkevich@yandex.ru',
    url='https://github.com/Solborm',
    python_requires='>=3.7',
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"],
    install_requires=['feedparser', 'ebooklib', 'lxml'],
    entry_points={
        "console_scripts": [
            "rss-reader = RssReader.menu:main",
        ]
    }
)
