import setuptools

with open("README.md", mode="r") as fd:
    long_description = fd.read()

setuptools.setup(
    name="slack-logger",
    version="0.9.0",
    author="Chaitanya Chinni",
    description="Slack Logger is a custom message logger to Slack for Python 3+",
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chinnichaitanya/python-slack-logger",
    packages=setuptools.find_packages(),
    install_requires=["slackclient == 2.7.1", "pyyaml == 5.3.1"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3",
)
