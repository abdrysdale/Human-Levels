from setuptools import setup

setup(
    name='humanLevels',
    version='0.1',
    py_modules=['humanLevels'],
    entry_points={
        'console_scripts':['humanLevels = humanLevels:run']
    },
)
        
