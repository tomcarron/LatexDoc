from setuptools import setup, find_packages


setup(
    name="LaTeXDoc",
    version="0.1.0",
    author="Tom Carron",
    author_email="tomocarron@gmail.com",
    description="Python module for generating simple LaTeX documents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tomcarron/LaTeXDoc",
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here.
        # For example:
        # 'numpy>=1.18.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
