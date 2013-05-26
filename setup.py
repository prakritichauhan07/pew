#! /usr/bin/env python

from setuptools import setup
import invewrapper

long_desc = '''Invewrapper is a set of tools to manage multiple virtual environments. It is written in pure python and leverages inve: the idea/alternative implementation of a better activate script.

The advantage is that invewrapper doesn't hook into a shell, but is only a set of commands that is thus completely shell-agnostic:

It works on bash, zsh, fish, powershell, etc.

For the documentation, you might want to read here:
https://github.com/berdario/invewrapper#usage'''

setup(
	name='invewrapper',
	version='0.1.3',
	description='tools to manage multiple virtualenvs written in pure python',
	long_description=long_desc,
	keywords='virtualenvwrapper',
	author='Dario Bertini',
	author_email='berdario+pypi@gmail.com',
	url='https://github.com/berdario/invewrapper',
	license='MIT License',
	packages=['invewrapper'],
	install_requires=['virtualenv', 'virtualenv-clone'],
	package_data={'': ['inve']},  # XXX
	entry_points={
		'console_scripts':
			["{0} = invewrapper.invewrapper:{0}_cmd".format(cmd[:-4])
			for cmd in dir(invewrapper.invewrapper) if cmd.endswith("_cmd")]},
	classifiers=[
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
		'Intended Audience :: Developers',
		'Environment :: Console']
)
