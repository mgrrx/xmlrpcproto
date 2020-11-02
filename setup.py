from setuptools import find_packages, setup

setup(
    name="xmlrpcproto",
    version="0.1.0",
    author="Markus Grimm",
    license="MIT",
    description="Sans I/O xmlrpc library",
    long_description="Sans I/O xmlrpc library",
    platforms="all",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,
    zip_safe=False,
    package_data={"xmlrpcproto": ["py.typed", "xmlrpc.rng"]},
    packages=find_packages(exclude=("tests",)),
    install_requires=("lxml"),
    python_requires=">=3.5",
)
