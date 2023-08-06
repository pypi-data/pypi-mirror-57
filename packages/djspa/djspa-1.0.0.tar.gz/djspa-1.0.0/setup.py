import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="djspa", # Replace with your own username
    version="1.0.0",
    author="Manuel Stingl",
    author_email="opensource@voltane.eu",
    description="Django addon for a single page application with dynamically loaded pages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.voltane.eu/voltane/pypi/djspa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
