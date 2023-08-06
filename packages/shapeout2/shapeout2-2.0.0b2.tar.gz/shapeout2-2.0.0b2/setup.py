from os.path import dirname, realpath, exists
from setuptools import setup, find_packages
import sys


author = u"Paul Müller"
authors = [author]
description = 'User interface for real-time deformability cytometry (RT-DC)'
name = 'shapeout2'
year = "2019"

sys.path.insert(0, realpath(dirname(__file__))+"/"+name)
from _version import version

setup(
    name=name,
    author=author,
    author_email='dev@craban.de',
    url='https://github.com/ZELLMECHANIK-DRESDEN/ShapeOut2',
    version=version,
    packages=find_packages(),
    package_dir={name: name},
    include_package_data=True,
    license="GPL v3",
    description=description,
    long_description=open('README.rst').read() if exists('README.rst') else '',
    install_requires=["appdirs",
                      "dclab>=0.19.0",
                      "fcswrite>=0.5.1",
                      "h5py>=2.8.0",
                      "numpy>=1.9.0",
                      "pyqt5",
                      "pyqtgraph>=0.10.0",
                      # using this will make it impossible to upload to PyPI:
                      #"pyqtgraph @ git+https://github.com/pyqtgraph/pyqtgraph.git@1ec175385e31c4e1e8dbe829b4387e4ac560082c",
                      "scipy>=0.13.0"],
    python_requires='>=3.6, <4',
    setup_requires=['pytest-runner'],
    tests_require=["pytest", "pytest-qt"],
    entry_points={"gui_scripts" : ['shapeout2 = shapeout2.__main__:main']},
    keywords=["RT-DC", "deformability", "cytometry", "zellmechanik"],
    classifiers= ['Operating System :: OS Independent',
                  'Programming Language :: Python :: 3',
                  'Intended Audience :: Science/Research',
                  ],
    platforms=['ALL']
    )

