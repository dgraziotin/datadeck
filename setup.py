# from ez_setup import use_setuptools
# use_setuptools()
from setuptools import setup, find_packages
from datadeck import __version__, __license__, __description__
__description_long__ = open('README').read()

setup(
    name='datadeck',
    version=__version__,
    # metadata
    author='Daniel Graziotin',
    author_email='d@danielgraziotin.it',
    license=__license__,
    description=__description__,
    long_description=__description_long__,
    keywords='data, packaging, component, tool, GUI',
    url='http://task3.cc/projects/datadeck',
    classifiers=[
    ],

    packages = find_packages(),  # include all packages under src
    package_data={
      'datadeck.res': ['*.txt']
    },
    include_package_data=True,
    install_requires=[
        'setuptools>=0.6c',
        # make ckan support obligatory for time being
        #'dpm>=0.10a',
	    'wxpython>2.8.9.1', # this is the version I used, may work with precedent versions
    ],
    test_suite='nose.collector',
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'datadeck = datadeck.main:run',
        ]
    },
)
