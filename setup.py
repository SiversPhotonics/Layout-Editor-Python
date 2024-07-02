import os

from setuptools import find_packages, setup

package_data = {}

if os.name == "posix":
    package_data = {"": ["*.so", "py.typed", "platforms/*"]}
elif os.name == "nt":
    package_data = {"": ["*.pyd", "py.typed", "platforms/*"]}

setup(
    name="layout_editor",
    version="1.0.2",
    include_package_data=True,
    packages=find_packages(),
    description="A layout editor package",
    author="Matthew McKee",
    author_email="matthew.mckee@sivers-photonics.com",
    package_data=package_data,
)
