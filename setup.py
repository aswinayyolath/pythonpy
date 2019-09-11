from setuptools import setup 

def readme():
	with open('README.md') as source:
		read_me = source.read()
	return read_me

setup(
	name="show_weather_data",
	version="0.0.1",
	description="A python package to get weather reports",
	long_description=readme(),
	long_description_content_type="text/markdown",
	url="https://github.com/aswinayyolath/pythonpy",
	author="Aswin A",
	author_email="aswin6303@gmail.com",
	classifiers=[
	
	"Programming Language :: Python :: 3",
	"Programming Language :: Python :: 3.7"],
	packages=["show_weather_data"],
	include_package_data=True,
	install_requires=["requests",  "pandas", "bs4"],
	)
