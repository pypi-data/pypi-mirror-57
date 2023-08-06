from setuptools import setup, find_packages


with open('README.md', 'rt') as f:
    ld = f.read()


setup(
    name='varseries',
    version='2.0.3',
    license='MIT',
    author='Cyrille Kossyguine',
    author_email='lambda_man@outlook.fr',
    description='An utility to build and display variation series',
    long_description=ld,
    long_description_content_type='text/markdown',
    url='https://github.com/cyrillelamal/varseries',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        'plotly>=4.3.0',
    ],
)
