from setuptools import find_packages, setup

setup(    # replace all <> with your own metadata
    name = '<name of tool>',
    version = '0.0.1',
    author = '<name of author>',
    author_email = '<email of author>',
    license = '<the license you chose>',
    description = '<short description for the tool>',
    url = '<github url where the tool code will remain>',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires='>= <version after which it will work>',
    install_requires=[
        'flask',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    # Replace <cmd> with the command you want to use to call your tool
    # and set main:main to be the
    entry_points = '''
        [console_scripts]
        cmd=main:main
    '''
)
