from setuptools import setup

setup(
    name='Kimai-Python',
    version='0.1.0',
    description='Kimai REST Client for Python',
    packages=['kimai_python'],
    author='Kajetan Bancerz',
    author_email='kajetan.bancerz@gmail.com',
    url='https://github.com/kbancerz/kimai-python',
    license=open('LICENSE').read(),
    #long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        'requests>=2.22.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
