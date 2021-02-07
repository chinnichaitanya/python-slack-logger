import setuptools

with open("README.md", mode="r") as fd:
    long_description = fd.read()

setuptools.setup(
    name="python-slack-logger",
    version="0.10.0",
    author="Chaitanya Chinni",
    description="Slack Logger is a custom message logger to Slack for Python 3",
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chinnichaitanya/python-slack-logger",
    packages=setuptools.find_packages(),
    install_requires=["slackclient == 2.9.3", "pyyaml == 5.4.1"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.5",
    keywords=[
        "monitoring",
        "slack",
        "messaging",
        "logging",
        "health-check",
        "notification-service",
        "notification",
        "slack-api",
    ],
)
