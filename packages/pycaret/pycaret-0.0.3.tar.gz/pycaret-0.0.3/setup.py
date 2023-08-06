from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="pycaret",
    version="0.0.3",
    description="A Python package for supervised and unsupervised machine learning.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/pycaret/pycaret",
    author="Moez Ali",
    author_email="moez.ali@queensu.ca",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["pycaret"],
    include_package_data=True,
    install_requires=["pandas", "numpy", "seaborn", "matplotlib", "IPython", "joblib", 
                     "sklearn", "shap", "ipywidgets", "yellowbrick"]
)