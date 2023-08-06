from setuptools import setup
from setuptools.command.install import install


LONG_DESCRIPTION = """
See [mypy_boto3](https://pypi.org/project/mypy-boto3/) for more info.
"""


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        try:
            from mypy_boto3.main import maybe_build_index
        except (ImportError, ModuleNotFoundError):
            pass
        else:
            maybe_build_index()


setup(
    name="mypy-boto3-connect",
    version="1.10.38.1",
    packages=["mypy_boto3_connect"],
    url="https://github.com/vemel/mypy_boto3",
    license="MIT License",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description="Mypy-friendly boto3 1.10.38 type annotations for connect service.",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed",
    ],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    package_data={"mypy_boto3_connect": ["py.typed"]},
    install_requires=["typing_extensions; python_version < '3.8'",],
    extras_require={"master": ["mypy-boto3==1.10.38.1"]},
    zip_safe=False,
    cmdclass={"install": PostInstallCommand,},
)
