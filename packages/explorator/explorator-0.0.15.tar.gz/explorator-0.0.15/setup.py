import sys
import os
from setuptools import setup

sys.path.append(os.path.abspath("C:\\Users\\bzakh\\OneDrive\\Documents\\Python_Scripts\\workfolder\\datae\\explorator_library\\explorator"))

from general_info import _version

setup(
    name='explorator',
    version=_version,
    description='Package to quickly explore data in pandas dataframe',
    license='',
    packages=['explorator'],
    author='Boris Zakhir',
    author_email='bz@omnichannel.ru',
    keywords=['pandas','exploratory'],
    url=''
)
