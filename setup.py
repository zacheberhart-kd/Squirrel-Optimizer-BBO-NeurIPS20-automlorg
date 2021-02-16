from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name        = 'switching_squirrel',
    packages    = find_packages(),
    version     = '0.0.1',
    description = 'A Switching Hyperparameter Optimizer',
    long_description=long_description,
    install_requires=[
        'cython==0.29.21',
        'configspace==0.4.13',
        'psutil==5.7.2',
        'docutils',
        'pynisher==0.6.0',
        'threadpoolctl',
        'pyrfr',
        'sobol_seq',
        'lazy_import',
        'scikit-optimize==0.7.4',
        'pyaml>=16.9',
        'scikit-learn>=0.22.0',
        'emcee',
        'numpy>=1.7.1',
        'scipy==1.5.2',
        'smac==0.12.4'
    ]
)
