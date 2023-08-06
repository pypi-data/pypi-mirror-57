import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="savi",
    version="0.0.5",
    author="seba.savi",
    author_email="seba.manda98@gmail.com",
    description="Una ayuda para los de lic. en sistemas jajaj",
    long_description=long_description,
    long_description_content_type="text/markdown",    
    url="https://github.com/SebaSavino",
    packages=setuptools.find_packages(),
    license='MIT',
    entry_points={
        "console_scripts": [
            "culiao=savi:savi",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["numpy", "Click"],
)

