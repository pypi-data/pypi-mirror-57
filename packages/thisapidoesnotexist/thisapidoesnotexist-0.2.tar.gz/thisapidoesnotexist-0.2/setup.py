import setuptools

with open("README.md") as fh:
    long_description = fh.read()

with open('LICENSE.md') as f:
    license = f.read()

setuptools.setup(
    name='thisapidoesnotexist',
    version='0.2',
    author="Miguel Lopes",
    author_email="miguel.lopes.filho@protonmail.com",
    description='Api não oficial das páginas thispersondoesnotexist '
                'e thiscatdoesnotexist',
    #long_description=long_description,
    long_description_content_type="text/markdown",
    license=license,
    url="https://github.com/Arfafa/ThisApiDoesNotExist",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
