from setuptools import setup, find_packages

setup(
    name="panelagent",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "langchain",
        "langchain-ollama",
        "langchain-chroma",
        "gradio"
    ],
    entry_points={
        "console_scripts": [
            "panelagent=main:cli",
        ],
    },
)