import os

from setuptools import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Avoids IDE errors, but actual version is read from version.py
__version__ = None
with open('chat/version.py') as f:
    exec(f.read())

# Get the long description from README file
with open(os.path.join(BASE_DIR, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

dev_requires = ['black==19.10b0']

tests_requires = ['pytest~=5.1', 'pytest-asyncio~=0.10', 'pytest-cov~=2.7']

install_requires = ['django<3.0', 'channels~=2.3.1', 'channels-redis~=2.4.1']

extras_requires = {
    'dev': dev_requires,
    'test': tests_requires,
    'docs': ['Sphinx~=2.1.2', 'recommonmark~=0.4.0'],
}

setup(
    name='djChat',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
    ],
    packages=find_packages(exclude=['docs', 'contrib', 'tests', 'tools', 'scripts']),
    entry_points={'console_scripts': ['pyeraser=pyeraser.__main__:main']},
    version=__version__,
    install_requires=install_requires,
    tests_require=tests_requires,
    extras_require=extras_requires,
    include_package_data=True,
    description='Chat application.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='a.Signz',
    author_email='a.Signz089@googlemail.com',
    maintainer='a.Signz',
    maintainer_email='a.Signz089@googlemail.com',
    license='GPLv3+',
    keywords='',
    url='https://gitlab.com/Django.apps/djchat',
    project_urls={
        'Bug Reports': 'https://gitlab.com/Django.apps/djchat/issues',
        'Source': 'https://gitlab.com/Django.apps/djChat.git',
    },
)
