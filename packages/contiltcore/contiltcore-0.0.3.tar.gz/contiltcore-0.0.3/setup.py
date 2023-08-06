from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["PyMySQL==0.9.3", "mysqlclient==1.4.2"]

setup(
    name="contiltcore",
    version="0.0.3",
    author="Contilt",
    author_email="info@contilt.com",
    description="Contilt Infrastructure",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/your_package/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
)