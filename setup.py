import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='PyPoint',
	version='1.0.0',
	author='Gary Haag',
	author_email='Haagimus@gmail.com',
	description='Point class with Cartesian and Polar coordinate support and conversions',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/Haagimus/py_point',
	packages=setuptools.find_packages(),
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Operating System :: OS Independent',
		'Topic :: Scientific/Engineering :: Mathematics'
	]
)