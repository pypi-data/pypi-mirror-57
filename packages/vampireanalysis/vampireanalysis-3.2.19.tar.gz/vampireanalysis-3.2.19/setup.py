import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vampireanalysis",
    version="3.2.19",
    author="Kyu Sang Han",
    author_email="khan21@jhu.edu",
    description="Vampire Image Analysis Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://wirtzlab.johnshopkins.edu",
    packages=setuptools.find_packages(),
    install_requires=[
        'scipy==1.2.2',
        'pandas==0.24.2', 
        'numpy==1.16.5', 
        'pillow==6.2.1',
        'matplotlib==2.2.4', 
        'scikit-learn==0.20.4', 
        'scikit-image==0.14.5',
        'opencv-python==4.1.2.30',
        'dask==1.2.2'
    ],
    scripts=['bin/vampire.py'],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        'Operating System :: Microsoft :: Windows',
        "Operating System :: MacOS :: MacOS X"
    ],
    python_requires='>=2.6'
)