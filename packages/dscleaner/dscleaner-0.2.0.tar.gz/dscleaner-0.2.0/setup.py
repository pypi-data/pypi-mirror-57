import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt","r") as req:
    inst_req = req.read()
setuptools.setup(
    name='dscleaner',
    version='0.2.0',
    author='Manuel Pereira',
    author_email='afonso.pereira4525@gmail.com',
    packages=['dscleaner',],
    project_urls={
        "Documentation": "https://dscleaner.rtfd.io/",
        "Source code": "https://gitlab.com/ManelPereira/dscleaner",
        "Examples": "https://osf.io/vraqz/",
    },
    license='The MIT License',
    description='A Python Library to Clean, Preprocess and Convert audio datasets',
    long_description=long_description,
    install_requires=inst_req,
)