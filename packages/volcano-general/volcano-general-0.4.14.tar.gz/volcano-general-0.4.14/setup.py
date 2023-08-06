from setuptools import setup

with open('version.txt') as f:
    ver = f.read().strip()

setup(
    name='volcano-general',
    version=ver,
    description='Volcano basic utilities',
    author='Vinogradov D',
    author_email='dgrapes@gmail.com',
    license='MIT',
    packages=['volcano.general'],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
