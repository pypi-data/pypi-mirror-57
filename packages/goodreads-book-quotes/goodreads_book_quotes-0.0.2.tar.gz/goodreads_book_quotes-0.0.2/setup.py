import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="goodreads_book_quotes",
    version="0.0.2",
    author="Yunzhi Gao",
    author_email="gaoyunzhi@gmail.com",
    description="Given book name, this library will find quotes from goodreads.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gaoyunzhi/goodreads_quotes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'bs4',
    ],
    python_requires='>=3.0',
)