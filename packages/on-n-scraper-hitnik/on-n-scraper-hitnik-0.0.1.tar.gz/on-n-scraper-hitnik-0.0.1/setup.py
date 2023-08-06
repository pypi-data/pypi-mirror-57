import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="on-n-scraper-hitnik",
    version="0.0.1",
    author="Aleksandr Nikitin",
    author_email="hitnik@gmail.com",
    description="Onliner news scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hitnik/onl_news_scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)