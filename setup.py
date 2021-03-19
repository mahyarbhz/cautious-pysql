from setuptools import setup
setup(
    name='ctpysql',
    version='0.0.1',
    description='This library is for run MYSQL queries as fast as possible 🚄🔥!',
    py_modules=["ctpysql"],
    package_dir={'': 'src'},
    install_requires = [
        "mysql-connector ~= 2.2.9",
        "mysql-connector-python ~= 8.0.23",
    ],
    url="https://github.com/MahyarNV/cautious-pysql",
    author="Mahyar Behzadi",
    author_email="mahyarbhz@gmail.com"
)
