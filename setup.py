 
from setuptools import find_packages ,setup 
from typing import List 

def get_requirements()->List[str]: 

    requirement_lst =[]
    try: 
        with open('requirements.txt' , 'r')  as f: 

            lines = f.readlines() 
            for line in lines: 
                requirement = line.strip()  

                if requirement and requirement != '-e .': 
                    requirement_lst.append(requirement)
    except FileNotFoundError: 
        print(f"File Not Found Error") 

    return requirement_lst 


setup( 
    name="NetworkSecurity" , 
    version='0.0.1'  , 
    author= 'Rohit Katkar',
    author_email='katkarrohit203@gmail.com' ,
    packages=find_packages() ,
    install_requires = get_requirements()
)
