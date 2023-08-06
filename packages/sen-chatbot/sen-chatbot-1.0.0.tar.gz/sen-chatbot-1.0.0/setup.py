from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="sen-chatbot",
    version="1.0.0",
    description="A Python package for creating chatbot.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/bubai666sen/sen-chatbot",
    author="Sourav Sen",
    author_email="bubai666sen@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["sen-chatbot"],
    include_package_data=True,
    install_requires=["wikipedia"],
)