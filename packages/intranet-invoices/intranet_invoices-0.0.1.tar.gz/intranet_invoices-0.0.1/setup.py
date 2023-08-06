import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="intranet_invoices", # Replace with your own username
    version="0.0.1",
    author="Som Mobilitat",
    author_email="admin@sommobilitat.coop",
    description="Module REST to display invoices",
    url="https://gitlab.com/sommobilitat/intranet_invoices",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
