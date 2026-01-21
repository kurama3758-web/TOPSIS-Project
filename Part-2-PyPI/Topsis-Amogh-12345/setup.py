from setuptools import setup

setup(
    name="Topsis-Amogh-12345",
    version="1.0.0",
    author="Amogh Singh",
    description="TOPSIS decision making package",
    packages=["topsis_amogh"],
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=topsis_amogh.topsis:main"
        ]
    },
)
