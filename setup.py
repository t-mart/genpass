from setuptools import setup, find_packages

setup(
        name='genpass',
        version='0.1',
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
