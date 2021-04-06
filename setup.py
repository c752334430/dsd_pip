import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dsd-tianyi",
    version="0.0.3",
    author="Tianyi Chen",
    author_email="ctianyi7@gmail.com",
    description="Dense subgraph discovery",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tsourolampis/dense-subgraph-discovery",
    project_urls={
        "Bug Tracker": "https://github.com/tsourolampis/dense-subgraph-discovery/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['dsd'],
    install_requires=[
          'networkx',
      ],
    python_requires=">=3.6",
)