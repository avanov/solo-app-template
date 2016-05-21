import os

from pathlib import Path
from setuptools import setup
from setuptools import find_packages


here = Path(os.path.abspath(os.path.dirname(__file__)))

with here.joinpath('README.rst').open() as f:
    README = f.read()

with here.joinpath('requirements.txt').open() as f:
    rows = f.read().strip().split('\n')
    requires = []
    for row in rows:
        row = row.strip()
        if row and not (row.startswith('#') or row.startswith('http')):
            requires.append(row)


# Setup
# ----------------------------

setup(name='{{cookiecutter.repo_name}}',
      version='{{cookiecutter.version}}',
      description='{{cookiecutter.project_short_description}}',
      long_description=README,
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'License :: OSI Approved',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Operating System :: POSIX',
          'Topic :: Internet :: WWW/HTTP',
      ],
      author='{{cookiecutter.author}}',
      author_email='{{cookiecutter.author_email}}',
      url='{{cookiecutter.project_url}}',
      keywords='web solo',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='tests',
      tests_require=['pytest', 'coverage'],
      install_requires=requires,
    )
