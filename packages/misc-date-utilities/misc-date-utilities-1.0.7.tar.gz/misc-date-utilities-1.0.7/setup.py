import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="misc-date-utilities",
    version="1.0.7",
    description="Date subtraction, parsing, and random timestamp generation.",
    author="Kevin Traw",
    author_email="ktraw2@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ktraw2/misc-date-utilities",
    packages=["misc_date_utilities","misc_date_utilities/tests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["dateutil"],
)
