import setuptools
from os.path import join, dirname

setuptools.setup(
    name="dbhub",  # Replace with your own username
    version="0.0.2",
    author="Noxormy",
    author_email="noxormy@gmail.com",
    description="Package to create db in one-click",
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Noxormy/dbhub_pip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
