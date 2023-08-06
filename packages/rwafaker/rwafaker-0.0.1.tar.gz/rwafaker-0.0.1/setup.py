from setuptools import setup
from os import path
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name="rwafaker",
  version='0.0.1',
  description="This package generates massive amounts of realistic fake data in Rwanda native language (Ikinyarwanda)",
  long_description=long_description,
  py_modules=["rwafake"],
  package_dir={'': 'rwafake'},
  keywords=['rwanda', 'faker', 'fake', 'rwafake'],
  python_requires=">=3.6",
  classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.7",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Operating System :: OS Independent",
      ],
      author='Igwaneza Bruce',
      author_email='knowbeeinc@gmail.com',
      license='MIT',
      zip_safe=False,

)
