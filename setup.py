from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="bleedfacedetector",
    version="1.0.0",
    description="A Python package that lets users use 4 different face detectors",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/TahaAnwar/bleedfacedetector",
    author="Taha Anwar",
    author_email="taha@bleedai.com",
    license="BSD",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["bleedfacedetector"],
    include_package_data=True,
    install_requires=["dlib","opencv-python","numpy"],
    
)