from setuptools import setup

setup(
    name='githubtestorg2-testrepo-testpkg',
    version='0.0.7.dev2',
    description="A sample Python project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/githubtestorg2/testrepo",
    install_requires=[
        'numpy>=1.11.0',
        'scipy',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    license='MIT',
)
