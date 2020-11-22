import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="console-tools-SombraCancelada",  # Replace with your own username
    version="0.0.1",
    author="Arturog",
    author_email="sombracancelada@gmail.com",
    description="Tools for console programs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SombraCancelada/consoleTools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
