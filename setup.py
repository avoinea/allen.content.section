from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='allen.content.section',
      version=version,
      description="allen section content-type",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='allen content zope3',
      author='Alin Voinea',
      author_email='alin.voinea@gmail.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['allen', 'allen.content'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-,
          'allen.content.core'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
