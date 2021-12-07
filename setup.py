import setuptools
import subprocess


description = (
    "This library contain random functions that are useful for python developers"
)
long_description = "There are a lot of functions that most of the python guys repeatedly \
google search, this library documents those functions and makes it in a ready to use form \
inside a library. There is no learning curve or anything for this library, just search your \
intended use case in the documentation, find the function, pass in the function arguements \
as given in the documentation and wait for the outputs :)"

library_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

setuptools.setup(
    name="random-functions",
    version=library_version,
    author="Bipin Krishnan P",
    author_email="bipinkrishnan1999.bk@gmail.com",
    license="MIT",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bipinkrishnan/random-functions",
    packages=setuptools.find_packages(),
    keywords=[],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[],
)
