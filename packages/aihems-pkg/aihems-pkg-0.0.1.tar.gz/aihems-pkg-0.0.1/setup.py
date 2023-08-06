import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aihems-pkg",  # Replace with your own username
    version="0.0.1",
    author="byungjin0826",
    author_email="byungjin0826@gmail.com",
    description="AIHEMS",
    long_description=long_description,
    url="https://github.com/byungjin0826/ai-hems-new",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)