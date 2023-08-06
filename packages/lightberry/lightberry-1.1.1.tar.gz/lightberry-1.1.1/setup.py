import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lightberry",
    use_scm_version = True,
    author="Sam Clark",
    author_email="slc2015@icloud.com",
    description="Lightberry Libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.samclark.me/",
    packages=['lightberry'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'paho-mqtt',
        'pycryptodome'
    ],
    setup_requires=[
        'setuptools_scm',
    ]
)
