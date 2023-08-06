import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MkRecClient",
    version="0.0.3",
    author="Mark Cartagena",
    author_email="mark@mknxgn.com",
    description="MkNxGn Client for MkRec. Free for use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://mknxgn.com/",
    requires=['mknxgn_essentials', 'requests'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)