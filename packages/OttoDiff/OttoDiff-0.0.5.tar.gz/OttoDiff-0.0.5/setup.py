import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OttoDiff",
    version="0.0.5",
    scripts=['OttoDiff/forward/forward.py'],
    author="Dan Park, Paul-Emile Landrin, Yaoyang Lin, Kyra Ballard",
    author_email="dpark@mba2020.hbs.edu, plandrin@g.harvard.edu,"+\
                 "yaoyanglin@g.harvard.edu, kballard@g.harvard.edu",
    description="Package used for automatic differentiation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CreativeAutomaticDifferentiators/cs207-FinalProject/archive/0.0.5.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
