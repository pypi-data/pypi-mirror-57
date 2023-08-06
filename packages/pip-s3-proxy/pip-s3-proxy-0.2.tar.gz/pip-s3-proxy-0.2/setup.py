from setuptools import setup


setup(
    name='pip-s3-proxy',
    version='0.2',
    description=('provides an unauthenticated plain HTTP proxy'
                 ' so pip can install packages from S3'),
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author='Toby Cabot (based on work by Rob Helmer)',
    author_email='toby@caboteria.org',
    license='MPL',
    url='https://github.com/caboteria/pip-s3-proxy',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    packages=['proxy'],
    include_package_data=True,
    keywords=['caching', 'lru', 's3', 'proxy', 'unauthenticated'],
    install_requires=['boto3>=1.6.22'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['nose', 'coverage', 'line_profiler', 'flake8'],
    },
    entry_points={
        'console_scripts': [
            'pip-s3-proxy = proxy.run:main',
            'pipsss = proxy.run:pipsss'
        ],
    },
    test_suite='nose.collector',
    zip_safe=False,
)
