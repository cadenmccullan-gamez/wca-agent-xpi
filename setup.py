from setuptools import setup, find_packages

setup(
    name="wca-agent-xpi",
    version="1.0.0",
    packages=find_packages(),
    description="World Class Assistant Agent eXecution and Programming Interface",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Caden McCullan-Gamez",
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
)
