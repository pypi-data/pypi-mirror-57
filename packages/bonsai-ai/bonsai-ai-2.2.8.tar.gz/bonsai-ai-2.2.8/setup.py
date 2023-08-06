import logging
from setuptools import setup, find_packages

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
log.debug('Running setup...')

version = {}
with open("./bonsai_ai/version.py") as fp:
    exec(fp.read(), version)
setup(
    name="bonsai-ai",
    version=version['__version__'],
    description="Simulator interface library for Bonsai AI platform v2",
    long_description=open('README.rst').read(),
    # url='https://github.com/BonsaiAI/bonsai-python',
    url="https://bons.ai",
    author="Bonsai, Inc.",
    author_email='opensource@bons.ai',
    license="BSD",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English'
    ],
    keywords="bonsai",
    install_requires=[
        'wheel>=0.31.0',
        'protobuf>=3.0.0,<4',
        'requests>=2.11',
        'yarl==1.2.0',
        'configparser>=3.5.0',
        'async_timeout==2.0.1',
        'aiohttp==2.3.10',
        'msal>=0.8.0',
    ],
    python_requires='>=3.5',
    packages=find_packages(),
)
