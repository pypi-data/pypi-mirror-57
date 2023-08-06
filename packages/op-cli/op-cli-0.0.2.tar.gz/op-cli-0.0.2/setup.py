from setuptools import setup, find_packages
from io import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]
setup (
	name = 'op-cli',
	description = 'A Simple command line',
	version = '0.0.2',
	packages = find_packages(), # list of all packages
    install_requires = install_requires,
    python_requires='>=2.7', # any python greater than 2.7
	entry_points='''
        [console_scripts]
        op-cli=op_cli.main:main
    ''',
	author="Oyetoke Toby",
	keyword="click, snap, cli, cla",
	long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
	include_package_data=True,
    url='https://gitlab.com/oyetoketoby80/elias-cli.git',
	download_url='https://gitlab.com/oyetoketoby80/elias-cli.git',
    dependency_links=dependency_links,
    author_email='oyetoketoby80@gmail.com',
	)

# pip install wheel 
# 	