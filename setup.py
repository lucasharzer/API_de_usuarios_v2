from setuptools import setup, find_packages

with open("requirements.txt") as r:
    install_requires = r.read()

setup(
    name = "API_de_usuarios_v2",
    version = "0.0.1",
    description = "Rest API with Python and Flask with database using SQLAlchemy",
    url = "https://github.com/lucasharzer/API_de_usuarios_v2",
    author = "Lucas Harzer",
    author_email = "lucasmatos592@gamil.com",
    license = "BSD",
    packages = find_packages(),
    install_requires = [install_requires],
    zip_safe = "False"
)