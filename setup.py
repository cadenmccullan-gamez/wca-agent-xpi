"""Compatibility package entry point.

Canonical project metadata is maintained in pyproject.toml.
Authorship: Alexis M. Adams
"""

from pathlib import Path

from setuptools import find_packages, setup


setup(
    name="wca-agent-xpi",
    version="1.3.1",
    packages=find_packages(),
    description="Axiom Hive Technology policy and privacy control library.",
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="Alexis M. Adams",
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
)
