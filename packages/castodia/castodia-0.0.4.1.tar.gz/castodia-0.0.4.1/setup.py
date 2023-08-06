import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="castodia",  # Replace with your own username
    version="0.0.4.1",
    author="Ayazhan Zhakhan",
    author_email="az@sanau.co",
    description="Castodia package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ayazhan-sanau/CastodiaProduct",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy', 'pandas', 'scipy', 'requests'
    ],  # specify which packages are required
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
