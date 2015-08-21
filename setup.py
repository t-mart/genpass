from setuptools import setup, find_packages

import genpass

setup(
        name='genpass',
        version=genpass.__version__,
        author=genpass.__author__,
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            "click==4.0",
        ],
        entry_points={
            'console_scripts': [
                'genpass=genpass.genpass:genpass',
            ],
        }
)
