'''
PyPi setup script.
'''

from setuptools import find_packages, setup

from luculia import VERSION_NUMBER

setup(
    name         = 'luculia',
    version      = VERSION_NUMBER,
    keywords     = 'personal command-line note databse',
    description  = 'A personal note-taking engine.',
    author       = 'Stephen Malone',
    author_email = 'mail@luculia.org',

    long_description = open('readme.md').read(),
    long_description_content_type = 'text/markdown',

    packages         = find_packages(exclude=['*tests*']),
    python_requires  = '>=3.8.0',
    install_requires = ['Click>=7.0', 'toml>=0.10.0'],

    entry_points = {'console_scripts': ['luculia=luculia.__main__:main']},
    project_urls = {
        'Changelog': 'https://github.com/luculia/luculia/blob/master/changes.md',
        'Issues':    'https://github.com/luculia/luculia/issues',
        'License':   'https://github.com/luculia/luculia/blob/master/license.md',
        'Releases':  'https://github.com/luculia/luculia/releases',
    },

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Topic :: Database',
    ],
)
