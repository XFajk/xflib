from setuptools import setup, find_packages

setup(
    name='xfps',
    version='0.1.8',
    description='A particle system and effects library for Pygame',
    author='XFajk',
    author_email='ertyperty24@gmail.com',
    url='https://github.com/XFajk/xfps/tree/main',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
    ],
    install_requires=[
        'pygame-ce',
    ],
)
