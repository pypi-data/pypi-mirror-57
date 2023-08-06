from setuptools import setup

setup(
    name='expi_skel',
    version='0.3',
    author='2665093 Ontario Inc.',
    url='https://2665093.ca',
    author_email='author@2665093.ca',
    packages=['expi_skel'],
    description='A package template for use with the Extender Package Index.',
    long_description="""
        The expi-skel package provides a template for creating Python packages
        that take advantage of the features of the `Extender Package Index
        (expi)`__. The package extensions supported by expi are documented
        in the `expi Package Format`_ document.

        .. __: https://expi.2665093.ca/
        .. _expi Package Format: https://expi.2665093.ca/package-format.html
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
