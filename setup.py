from setuptools import find_packages,setup
# from typing import list


#codeium: Refactor |Explain| Generaate Docstring| X
def get_requirements()->list[str]:

    requirements_list = list[str] =[]

    return requirements_list





setup(
name = 'sensor',
version = '0.0.1',
author = 'Suryakant Sahoo',
author_email='ssuryakanta789@gmail.com',
packages = find_packages(),

install_requires = get_requirements(),      #["pymongo"]

)