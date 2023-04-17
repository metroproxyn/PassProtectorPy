from setuptools import setup

setup(
    name="PassProtector",
    version="1.0",
    author="Aleks Mashanski",
    author_email="maszanski@yahoo.com",
    description="A password manager tool",
    packages=["passprotector"],
    install_requires=["cryptography==3.4.7"],
    entry_points={
        "console_scripts": [
            "passprotector = passprotector.main:main",
        ]
    }
)