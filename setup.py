from setuptools import setup, find_packages

setup(
    name="system_rezerwacji",  
    version="1.0.2",  
    packages=find_packages(),  
    install_requires=["Flask", "Flask-SQLAlchemy"],  
    description="System rezerwacji zasobów ",
    author="Miłosz Kordziński",
    author_email="miloszk.kontakt@gmail.com",
)
