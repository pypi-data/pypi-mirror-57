import setuptools

setuptools.setup(
    name="piClusterManager",
    version="0.0.2",
    author="Lukáš Plevač",
    author_email="lukasplevac@gmail.com",
    description="Open Source Pi Clusters manager",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/Lukas0025/PSNN",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    scripts=[
        'bin/picluster',
        'bin/piclusterdeamon'
    ],
    python_requires='>=3.0',
    install_requires=[
        'paramiko'
    ],
)
