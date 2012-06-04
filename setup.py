# -*- coding:utf-8 -*-
import os
from setuptools import setup, find_packages

version = '0.1'

setup(name='s17.content.suggestionbox',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "INSTALL.txt")).read() + "\n" +
                       open(os.path.join("docs", "CREDITS.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Plone :: 4.1",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='python plone zope simples_consultoria',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='http://www.simplesconsultoria.com.br',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['s17', 's17.content'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'plone.app.dexterity>=1.1',
        'plone.app.referenceablebehavior',
        'plone.app.relationfield',
        'plone.namedfile[blobs]',
        'collective.upload',
        'cioppino.twothumbs',
        ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
