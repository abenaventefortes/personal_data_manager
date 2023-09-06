from setuptools import setup, find_packages

setup(
    name="personal-data-manager",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyYAML",
        "setuptools",
        "beautifulsoup4"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={
        'console_scripts': [
            'personal-data-manager=personal_data_manager.main:main',
        ],
    },
)
a