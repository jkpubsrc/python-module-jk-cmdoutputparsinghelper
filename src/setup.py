################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 3 - Alpha",
		"Programming Language :: Python :: 3",
	],
	description = "Assists in parsing output of *nix system commands such as df, systemctrl and others.",
	include_package_data = False,
	install_requires = [
	],
	keywords = [
		"...",
	],
	license = "proprietary",
	name = "jk_cmdoutputparsinghelper",
	packages = [
		"jk_cmdoutputparsinghelper",
	],
	version = "0.2020.12.27",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
