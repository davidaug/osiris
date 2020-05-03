import setuptools
from setuptools.command.sdist import sdist

with open("README.md", "r") as fh:
    long_description = fh.read()


class Sdist(sdist):

    def run(self):
        self.run_command('compile_catalog')
        sdist.run(self)


setuptools.setup(
    name="osiris",
    version="0.0.5",
    author="David Veiga",
    author_email="david@david.blog.br",
    description="Validators for field",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davidaug/osiris",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)