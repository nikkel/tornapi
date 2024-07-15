from setuptools import setup, find_packages

setup(
    name='tornapi',
    version='0.2.0',
    description='A Python library for interacting with the Torn API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nikkel/tornapi',
    author='Ryan Clark',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
