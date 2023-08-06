from setuptools import setup, find_packages

setup(
	name='pensive',
	version='0.0.0',
	license='MIT',
	author='Idin',
	author_email='py@idin.ca',
	url='https://github.com/idin/pensive',
	keywords='graph',
	description='Python library for creating and drawing graphs and taking advantage of graph properties',
	long_description_content_type='text/markdown',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Topic :: Software Development :: Libraries :: Python Modules'
	],

	packages=find_packages(exclude=("jupyter_tests", ".idea", ".git")),
	install_requires=[],
	python_requires='~=3.6',
	zip_safe=True,
	test_suite='nose.collector',
	tests_require=['nose', 'coverage']
)
