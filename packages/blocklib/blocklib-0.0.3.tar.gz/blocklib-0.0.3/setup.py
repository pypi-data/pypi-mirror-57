import setuptools

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

requirements = [
    "jsonschema>=3.1.1",
    "Fuzzy>=1.2.2",
    "numpy>=1.17.2",
]

setuptools.setup(
    name="blocklib",
    version="0.0.3",
    author="Joyce Wang",
    author_email="joyce.wang@csiro.au",
    description="A library for blocking in record linkage",
    long_description=readme,
    long_description_content_type='text/x-rst',
    url='https://github.com/data61/blocklib',
    license='Apache',
    packages=setuptools.find_packages(),
    package_data={'blocklib': ['docs/schemas/*.json*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],

    install_requires=[
        "Fuzzy>=1.2"
    ],
    tests_require=[
        "pytest>=5.0",
    ]
)
