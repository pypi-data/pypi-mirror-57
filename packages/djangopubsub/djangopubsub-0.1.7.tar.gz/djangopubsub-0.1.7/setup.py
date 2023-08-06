from setuptools import setup, find_packages
from os import path

current_dir = path.abspath(path.dirname(__file__))

with open(path.join(current_dir, 'README.md')) as f:
    long_description = f.read()

setup(name='djangopubsub',
      version='0.1.7',
      description='Base redis pubsub django wrapper',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://gitlab.com/kas-factory/packages/django-pubsub',
      author='Antonio @ KF',
      author_email='antonio@kasfactory.net',
      license='COPYRIGHT',
      packages=find_packages(),
      package_data={'djangopubsub': ['djangopubsub/*',
                                     'djangopubsub/management/*',
                                     'djangopubsub/management/commands/*']},
      install_requires=[
            'Django>=1.8.18',
            'kfpubsub>=0.1.6'
      ],
      zip_safe=False
)
