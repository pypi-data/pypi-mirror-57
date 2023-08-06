import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eLearning", # Replace with your own username
    version="0.0.5",
    author="Ivan Y. Fernandez-Rosales",
    author_email="ifdezr@gmail.com",
    description="eLearning is an API dedicated to managing the backend infrastructure of an e-learning system.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ivanfdezr/DACODES-CHALLENGE",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.6',
)