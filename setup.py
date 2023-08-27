from setuptools import setup, find_packages

setup(
    name='sendcm',
    version='0.1',
    description='Python package to interact with the Send.cm API',
    author='Modd',
    author_email='immodded@proton.me',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    url='https://github.com/immodded/send-cm',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
