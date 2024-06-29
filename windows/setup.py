from setuptools import setup, find_packages

setup(
    name="layout_editor",
    version="1.0.1",
    include_package_data=True,
    packages=find_packages(),
    description="A layout editor package",
    author="Matthew McKee",
    author_email="matthew.mckee@sivers-photonics.com",
    install_requires=["numpy"],
    package_data={"": ["*.pyd", "py.typed"]},
)
