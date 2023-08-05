import setuptools

with open("README.md", "r") as fh:
    description_text = fh.read()

setuptools.setup(
  name='filetype_validator',
  packages=['filetype_validator'],
  version='0.2.2',
  license='MIT',
  description=description_text,
  author='isna',
  author_email='isna11583@gmail.com',
  url='https://github.com/ixna/filetype_validator',
  download_url='https://github.com/ixna/filetype_validator/releases/tag/v0.2.1',
  keywords=['filetype', 'extension'],
  dependency_links=['git+https://github.com/ixna/filetype.py'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
