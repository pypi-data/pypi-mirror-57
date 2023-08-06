# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['srtoffset']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['srtoffset = srtoffset.srtoffset:main']}

setup_kwargs = {
    'name': 'srtoffset',
    'version': '0.1.1',
    'description': 'Apply a time offset to a subtitle .srt file',
    'long_description': "Apply a time offset to a subtitle .srt file.\n\nExample:\n\n```console\n$ cat ~/example.srt\n1\n00:00:01,600 --> 00:00:04,200\nEnglish (US)\n\n2\n00:00:05,900 --> 00:00:07,999\nThis is a subtitle in American English\n\n3\n00:00:10,000 --> 00:00:14,000\nAdding subtitles is very easy to do\n$ srtoffset ~/example.srt '00:00:05,500'\n1\n00:00:07,100 --> 00:00:09,700\nEnglish (US)\n\n2\n00:00:11,400 --> 00:00:13,499\nThis is a subtitle in American English\n\n3\n00:00:15,500 --> 00:00:19,500\nAdding subtitles is very easy to do\n$ srtoffset ~/example.srt '00:00:01,000' --rewind\n1\n00:00:00,600 --> 00:00:03,200\nEnglish (US)\n\n2\n00:00:04,900 --> 00:00:06,999\nThis is a subtitle in American English\n\n3\n00:00:09,000 --> 00:00:13,000\nAdding subtitles is very easy to do\n```\n\n## Setup the dev environment\n\n```console\n$ poetry init\n$ poetry install\n```\n\n## Run the tests\n\n```console\n$ poetry run pytest\n```",
    'author': 'Balthazar Rouberol',
    'author_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
