# from ez_setup import use_setuptools
# use_setuptools()
from setuptools import setup, find_packages
from datapkg import __version__, __license__, __description__
__description_long__ = open('README').read()

setup(
    name='datapkg-gui',
    version=__version__,
    # metadata
    author='Daniel Graziotin',
    author_email='d@danielgraziotin.it',
    license=__license__,
    description=__description__,
    long_description=__description_long__,
    keywords='data, packaging, component, tool',
    url='http://task3.cc/projects/datapkg-gui',
    classifiers=[
    ],

    packages = find_packages(),  # include all packages under src
    #package_dir = {'':'datapkg-gui'},   # tell distutils packages are under src
    include_package_data=True,
    install_requires=[
        'setuptools>=0.6c',
        # make ckan support obligatory for time being
        'ckanclient>=0.3',
        'datapkg>=0.8'
    ],
    test_suite='nose.collector',
    zip_safe=False,
)
