import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="Get to the Show"
    version="0.0.1",
    author="your name",
    author_email="katherine.doris.mundale@gmail.com",
    url="https://github.com/kdmundale/App_GetToTheShow",
    description="My first text adventure game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
