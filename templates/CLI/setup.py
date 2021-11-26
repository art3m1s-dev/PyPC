from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:  # Use the README as the 'long description' of your tool
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:  # To read the packages your tool requires to function
    requirements = fh.read()

setup(                          # the <> tags and their contents must be replaced with your own metadata
    name = '<name of tool>',
    version = '0.0.1',
    author = '<name of author>',
    author_email = '<email of author>',
    license = '<the license you chose>',
    description = '<short description for the tool>',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = '<github url where the tool code will remain>',
    py_modules = ['main', 'app'],  # Change 'main' to be the name of your main file (without the '.py' extension)
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.6',             # Change the Python version required to the correct one
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
