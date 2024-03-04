from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:                     
    '''
    this func will return the list of requirements.
    '''  
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()     #this will read all lines of requirements.txt
        
        #but this may read the next line i.e \n in order to remove this....
        requirements=[req.replace("\n","") for req in requirements]


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return  requirements        






setup(
    name='mlproject',
    version='0.0.1',
    author='Rishi Ranjan',
    author_email='101rishidsr@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas', 'numpy', 'seaborn']                or
    install_requires=get_requirements('requirements.txt')

)