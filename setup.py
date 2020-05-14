from setuptools import find_packages, setup

setup(
    name="takathon",
    version="0.2.0",
    author="Piotr Piwoński",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["click>=7.1.2", "click-log>=0.3.2", "lark-parser>=0.8.5",],
    entry_points="""
        [console_scripts]
        takathon=takathon.cli:takathon
    """,
)
