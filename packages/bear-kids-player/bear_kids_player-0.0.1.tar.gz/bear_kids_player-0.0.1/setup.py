import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bear_kids_player", # Replace with your own username
    version="0.0.1",
    author="Shawn Wang",
    author_email="shawnyanwang@gmail.com",
    description="A player for kids",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shawnyanwang/bear_kids_player",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
