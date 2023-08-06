from setuptools import setup,find_packages

setup(name="SigProfilerTopography",
    version="0.3.13",
    author="Burcak Otlu",
    author_email="burcakotlu@eng.ucsd.edu",
    description="SigProfilerTopography provides topography analyses for substitutions, dinucleotides and indels for each sample and all samples pooled.",
    url="https://github.com/AlexandrovLab/SigProfilerTopography",
    license='UCSD',
    packages=find_packages(),
    install_requires=[
        "sigprofilermatrixgenerator>=1.0.21",
	"sigprofilersimulator>=0.2.15",
        "matplotlib>=2.2.2",
        "scipy>=1.1.0",
        "pandas>=0.23.4",
        "numpy>=1.14.3",
        "statsmodels>=0.9.0",
        "fastrand>=1.2",
        "twobitreader",
        "pyBigWig>=0.3.17",
        "psutil>=5.6.3"],
    include_package_data=True,
	zip_safe=False)
