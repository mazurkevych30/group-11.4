"""Setup file for CLI assistant"""
from setuptools import setup, find_namespace_packages

setup(
    name="assistant",
    version="0.1.0",
    description="CLI assistant",
    packages=find_namespace_packages(include=["src"]),
    install_requires=[
        "colorama==0.4.6",
        "prompt_toolkit==3.0.48",
        "wcwidth==0.2.13",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "run_assistant = src.main:main"
        ]
    },
)
