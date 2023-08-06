import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cdrive",
    version="0.0.1",
    author="Kaushik Chandrasekhar",
    author_email="kaushikc92@gmail.com",
    description="Python SDK for CDrive",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/columbustech/cdrive-sdk",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
