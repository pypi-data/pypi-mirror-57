import setuptools


setuptools.setup(
    name='fetch_dcos_token',
    version='0.9.7',
    author='Martijn Dekkers',
    author_email='pypi@dekkers.org.uk',
    description='Simple module to get a JWT token from a DC/OS master',
    url='https://github.com/m-dekkers/fetch_dcos_token',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=['fetch_dcos_token'],
    install_requires=['jwt', 'requests', 'datetime'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
