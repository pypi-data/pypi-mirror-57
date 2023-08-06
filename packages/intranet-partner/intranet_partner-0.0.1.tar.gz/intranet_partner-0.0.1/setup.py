import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="intranet_partner", # Replace with your own username
    version="0.0.1",
    author="Som Mobilitat",
    author_email="admin@sommobilitat.coop",
    description="Add fields to connect to intranet client area",
    url="https://gitlab.com/sommobilitat/intranet_partner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
