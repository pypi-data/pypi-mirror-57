from setuptools import setup

setup(
    name='sublogs',
    version='0.0.1',
    description=(
        '异步的日志组件，支持日志保存mongo'
        'Purely asynchronous high performance logging components，Support for mongo'
    ),
    long_description=open('README.rst', 'rb').read(),
    author='yuanYW',
    author_email='1030327908@qq.com',
    maintainer='yuanYW',
    maintainer_email='1030327908@qq.com',
    license='MIT',
    packages=['sublogs'],
    platforms=["all"],
    url='https://github.com/time-yuan/sublogs-master',
    install_requires=[
        'uvloop',
        'motor',
        'elasticsearch-async',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
