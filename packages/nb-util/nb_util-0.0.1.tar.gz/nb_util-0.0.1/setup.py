import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nb_util", # Replace with your own username
    version="0.0.1",
    author="jvansan",
    author_email="jeffreyavansanten@gmail.com",
    description="A simple wrapper around joblib for jupyter notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jvansan/nb_util",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "caffeine",
        "tqdm",
        "joblib",
    ]
)
