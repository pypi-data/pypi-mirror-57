from setuptools import setup



with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="CreditScoreCard",
    version="0.0.1",
    author="SimaShanhe",
    author_email="hsliu_em@126.com",
    description="risk control modeling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['CreditScoreCard'],
    install_requires=[
        'scikit-learn>=0.21.3',
        'scipy',
        'numpy',
        'matplotlib',
        'seaborn',
        'prettytable',
        'tqdm'
    ]
)