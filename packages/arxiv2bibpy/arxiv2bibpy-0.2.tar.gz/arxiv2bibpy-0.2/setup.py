import os
import setuptools

cwd = os.path.abspath(os.path.dirname(__file__))
requirements = open(cwd + "/requirements.txt").read().split("\n")

setuptools.setup(
    version="0.2",
    include_package_data=True,
    name="arxiv2bibpy",
    author="Duong Nhu",
    author_email="d.binhnhu@gmail.com",
    description="Search arxiv via api and save as bib",
    keywords="arxiv, bibtext, bib",
    url="https://github.com/code-fury/arxiv2bib",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    scripts=["arxiv2bib/arxiv2bib"],
    license="MIT",
)
