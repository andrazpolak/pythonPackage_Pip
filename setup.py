from setuptools import setup, find_packages

setup(
    name="example-pkg-andrazpolak",
    version="0.0.1",
    description="A small example package",
    url="https://github.com/andrazpolak/pythonPackage_Pip",
    author="Andraz Polak",
    author_email="andraz.polak@gmail.com",
    maintainer="Andraz Polak",
    maintainer_email="andraz.polak@gmail.com",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    include_package_data=True,
)
