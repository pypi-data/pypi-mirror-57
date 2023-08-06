from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="ifsc-expand",
    version="1.0.0",
    description="A Python package to get bank branch details from Indian Financial System Code(IFSC).",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/vil-c/ifsc-expand",
    author="Aman Kumar",
    author_email="amn9955@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=["ifsc_expand"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "ifsc-expand=ifsc_expand.__main__:main",
        ]
    },
)