from setuptools import setup, find_packages

setup(
    name='xfps',
    version='0.1.0',
    description='A particle system and effects library for Pygame',
    author='XFajk',
    author_email='ertyperty24@gmail.com',
    url='https://github.com/yourusername/pygame-particle-system',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'pygame',
    ],
)
