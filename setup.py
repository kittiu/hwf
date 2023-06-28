from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hwf/__init__.py
from hwf import __version__ as version

setup(
	name="hwf",
	version=version,
	description="HWF",
	author="Kitti U.",
	author_email="kittiu@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
