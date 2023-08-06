"""Setup for the arules package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Abir Koren",
    author_email="abir@wnwd.com",
    name='arules',
    license="MIT",
    description='multi-purpose association rules analysis',
    version='0.0.0',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/windward-ltd/arules',
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=['pandas','numpy'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)