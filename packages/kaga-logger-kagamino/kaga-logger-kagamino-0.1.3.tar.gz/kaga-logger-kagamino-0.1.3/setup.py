import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name="kaga-logger-kagamino",
    version="0.1.3",
    author="Martin Kagamino Lehoux",
    author_email="martin@lehoux.net",
    description="A simple colored logger for python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/martinlehoux/kaga-logger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.7"
)