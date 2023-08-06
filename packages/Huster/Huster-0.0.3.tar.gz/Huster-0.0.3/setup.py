# from distutils.core import setup
from setuptools import setup
from utils import copy_scripts_to_bin

copy_scripts_to_bin("./utils/build_server.py")

# setup(
#     name='Huster',
#     version='0.0.1',
#     author='ZQPei',
#     author_email='peiziqiang@gmail.com',
#     packages=['huster'],
#     url='https://github.com/ZQPei/Huster',
#     scripts=[],
#     description='HTTP Uploading Server Tool.',
#     install_requires=[],
# )


setup(
    name='Huster',
    version='0.0.3',
    author='ZQPei',
    author_email='peiziqiang@gmail.com',
    packages=['huster'],
    url='https://github.com/ZQPei/Huster',
    description='HTTP Uploading Server Tool.',
    long_description=open('./README.md', 'r').read(), 
    long_description_content_type="text/markdown",
    platforms=["all"],
    license='MIT',
)
