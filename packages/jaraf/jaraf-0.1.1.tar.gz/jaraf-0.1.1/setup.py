from setuptools import find_packages, setup

with open("../README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="jaraf",
    version="0.1.1",
    author="Edward Labao",
    author_email="edlabao.dev@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    description="Just another rakish application framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url="https://github.com/edlabao/jaraf",
    zip_safe=True
)
