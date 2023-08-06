from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="nanotopology",
    version="1.0.1",
    description="A Python package to check the similarity of two graphs using nanotopology.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/J-Kiruthika/Nanotopology",
    author="Kiruthika J",
    author_email="kiruthika.17cs@kct.ac.in",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["nano_topology"],
    include_package_data=True,
    python_requires='>=2.6',
)
