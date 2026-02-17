from setuptools import setup, find_packages

setup(
    name='Topsis-Prannay-102317125',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'topsis=Topsis_Prannay_102317125:main',
        ],
    },
    author='Prannay',
    author_email='pkamal_be23@thapar.edu',
    description='A python package for TOPSIS implementation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)