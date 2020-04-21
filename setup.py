from setuptools import setup

setup(
    name='keras-tcn-fork',
    version='3.0.2',
    description='Keras TCN',
    author='Philippe Remy',
    license='MIT',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    packages=['tcn_hyeche'],
    # manually install tensorflow or tensorflow-gpu
    install_requires=[
        'numpy>=1.18.1',
        'keras>=2.3.1',
        'gast==0.2.2'
    ]
)
