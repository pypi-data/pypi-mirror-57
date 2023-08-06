import sys
import traceback

from setuptools import setup
from setuptools.command.install import install


LONG_DESCRIPTION = """
See [mypy_boto3](https://pypi.org/project/mypy-boto3/) for more info.
"""


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        print("mypy_boto3: Running post-install script")
        try:
            from mypy_boto3.main import maybe_build_index

            maybe_build_index()
            print("mypy_boto3: Package index updated")
        except:
            print("mypy_boto3: Package index update failed", sys.exc_info())
            print(traceback.format_exc())


setup(
    name="mypy-boto3-route53resolver",
    version="1.10.39.5",
    packages=["mypy_boto3_route53resolver"],
    url="https://github.com/vemel/mypy_boto3",
    license="MIT License",
    author="Vlad Emelianov",
    author_email="vlad.emelianov.nz@gmail.com",
    description="Mypy-friendly boto3 1.10.39 type annotations for route53resolver service.",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed",
    ],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    package_data={"mypy_boto3_route53resolver": ["py.typed"]},
    install_requires=["typing_extensions; python_version < '3.8'",],
    zip_safe=False,
    cmdclass={"install": PostInstallCommand},
)
