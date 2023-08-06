from setuptools import setup

setup(
    name='expi_skel',
    version='0.1',
    author='2665093 Ontario Inc.',
    url='https://2665093.ca',
    author_email='author@2665093.ca',
    packages=['expi_skel'],
    description='A package template for use with expi.',
    long_description="""
        This is the long description of the package.  It can
        span multiple lines and include `rst`_.

        .. _rst: http://docutils.sourceforge.net/docs/ref/rst/directives.html
    """,
    install_requires=[
        'openpyxl',
        'markdown',
        'boto3',
    ],
    # Valid classifiers: https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.4",
    ],
    keywords=[
        "Orchid", "Extender", "Sage 300", "Automation",
    ],
    download_url="https://expi.2665093.ca/poplar/expi_skel",
)
