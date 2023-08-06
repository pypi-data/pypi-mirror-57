import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='model_selection',
    version='0.0.1',
    author="Manikandan Jeyabal",
    author_email="ManikandanJeyabal029@gmail.com",
    description="A Library which provides more information about suitable Machine learning algorithm for your dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ManikandanJeyabal/ChooseMyALGO",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
 )