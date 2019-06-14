from setuptools import setup




setup(
    name="bleedfacedetector",
    version="1.0.4.3",
    description="A Python package that lets users use 4 different face detectors",
    long_description='You can find the usage for this library here: "https://github.com/TahaAnwar/bleedfacedetector"',
    long_description_content_type="text/markdown",
    url="https://github.com/TahaAnwar/bleedfacedetector",
    author="Taha Anwar",
    author_email="taha@bleedai.com",
    license="BSD",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
		'Intended Audience :: Developers',     
        'Topic :: Software Development :: Build Tools',
		
    ],
    packages=["bleedfacedetector"],
    include_package_data=True,
    install_requires=["dlib==19.8.1","opencv-python","numpy"],
    
)