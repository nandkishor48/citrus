from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nextcitrus/__init__.py
from nextcitrus import __version__ as version

setup(
	name="nextcitrus",
	version=version,
	description="Test",
	author="Nand",
	author_email="Nand@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
