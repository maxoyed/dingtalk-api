import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="dingtalk-api",
    version="0.0.1",
    author="maxoyed",
    author_email="maxoyed@gmail.com",
    description="钉钉服务端 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maxoyed/dingtalk-api",
    packages=setuptools.find_packages(include=["dingtalk_api", "dingtalk_api.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
    ],
    python_requires=">=3.7",
)
