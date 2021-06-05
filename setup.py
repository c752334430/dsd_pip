import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dsd",
    version="0.0.2",
    author="C.E. Tsourakakis and Tianyi Chen",
    author_email="graphminingtoolbox@gmail.com",
    description="Dense subgraph discovery",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tsourakakis-lab",
    project_urls={
        "Bug Tracker": "https://github.com/tsourolampis/dense-subgraph-discovery/",
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
    python_requires=">=3.0",
)
