from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ctpysql',
    version='0.1.0',
    description='This library is for run MYSQL queries as fast as possible 🚄🔥!',
    py_modules=["ctpysql"],
    package_dir={'': 'src'},
    install_requires = [
        "mysql-connector >= 2.2.9",
        "mysql-connector-python >= 8.0.23",
    ],
    extras_require = {
        "dev": [
            "pytest>=6.2.2"
        ]
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MahyarNV/cautious-pysql",
    author="Mahyar Behzadi",
    author_email="mahyarbhz@gmail.com"
)
