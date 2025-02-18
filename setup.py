import setuptools

with open("README.md", mode="r") as fd:
    long_description = fd.read()

setuptools.setup(
    name="python-slack-logger",
    version="0.10.1",
    author="Chaitanya Chinni",
    description="Slack Logger is a custom message logger to Slack for Python 3",
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chinnichaitanya/python-slack-logger",
    packages=setuptools.find_packages(),
    install_requires=["slackclient == 2.9.4", "pyyaml == 6.0.1"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.6",
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
