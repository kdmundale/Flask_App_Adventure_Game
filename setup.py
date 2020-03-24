import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="GetToTheShow"
    version="0.0.1",
    author="Kate Mundale",
    author_email="katherine.doris.mundale@gmail.com",
    url="https://github.com/kdmundale/Flask_App_Adventure_Game",
    description="My first text adventure game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
