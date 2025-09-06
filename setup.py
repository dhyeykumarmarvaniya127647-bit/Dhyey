from setuptools import setup, find_packages

setup(
    name="signal_ICT_DhyeyMarvaniya_92400133061",
    version="0.1",
    author="DhyeyMarvaniya",
    author_email="dhyeykumar.marvaniya127647@marwadiuniversity.ac.in",
    description="Signal Generation and Operations package for demonstration",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
