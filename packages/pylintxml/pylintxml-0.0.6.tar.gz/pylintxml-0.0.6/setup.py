import glob
import os
from pathlib import Path
from setuptools import setup


setup(
    author='BPL.',
    author_email='',
    description='XML linter',
    include_package_data=True,
    install_requires = Path("requirements.txt").read_text().splitlines(),
    long_description= Path("README.md").read_text(),
    long_description_content_type='text/markdown',
    name='pylintxml',
    python_requires='>=3.6.0',
    version='0.0.6',
    entry_points={
        'console_scripts': [
            'pylintxml = pylintxml.main:main'
        ]
    },
    packages=[
        'pylintxml'
    ],
    license='MIT'
)
