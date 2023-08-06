import setuptools


# from pip.req import parse_requirements

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


install_reqs = parse_requirements("requirements.txt")
# print(install_reqs)
reqs = install_reqs

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="color2vec",
    version="1.0.1",
    author="chandan mishra",
    author_email="chandan.mishra@greendeck.co",
    description="Greendeck color to vector package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=['color2vec', 'color2vec.src', 'color2vec.src.data', 'color2vec.src.model'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=reqs,
    include_package_data=True,
    zip_safe=False
)
