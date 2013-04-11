from distutils.core import setup

packages = ['pyinvest']
required = ['numpy']

setup(
    name='pyinvest',
    version='dev',
    author='James Whinfrey',
    author_email='james@conceptric.co.uk',
    url='none',
    description='Tools for investment valuation',
    packages=packages,
    install_requires=required
)