from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name = 'mvpoly',
    version = '0.97.9',
    description = 'A library for multivariate polynomials',
    long_description = readme(),
    url = 'http://soliton.vm.bytemark.co.uk/pub/jjg/en/code/mvpoly/',
    author = 'J.J. Green',
    author_email = 'j.j.green@gmx.co.uk',
    license = 'LGPLv3',
    packages = ['mvpoly', 'mvpoly.util'],
    keywords = 'polynomial multivariate numeric RBF',
    zip_safe = True,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Mathematics'
    ],
    setup_requires = ['pytest-runner'],

    # scipy 1.2.0 causes a CI fail due to undeclared UTF-8
    # (see https://github.com/scipy/scipy/issues/9606,
    # from which "I suspect it will only happen on 2.7, which
    # we don't test now") and scipy 1.3.0 requires python 3.5
    # or later, so we have to do this silly dance of explicit
    # dependencies.  Python pacakging is the pits.

    install_requires = [
        'numpy>=1.7.0',
        'scipy<1.2.0;python_version<="3.4"',
        'scipy!=1.2.0;python_version>="3.5"'
    ],
    tests_require = [
        'hypothesis>=3.54.0',
        'pytest>=3.4.0',
        'pytest-cov>=2.5.0'
    ]
)
