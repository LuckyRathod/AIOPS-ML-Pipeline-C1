from setuptools import setup,find_packages

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Lucky",
    description="Sample Package for DVC ML  Pipleline c1",
    long_description=long_description,
    long_description_content_type ="text/markdown",
    url="https://github.com/LuckyRathod/AIOPS-ML-Pipeline-C1",
    author_email="luckyrathod46@gmail.com",
    #package_dir={"":"src"},
    #packages=find_packages(where="src"),license="GNU",
    packages=["src"],
    python_requires=">=3.6",
    install_requires=[
        'dvc',
        'dvc[gdrive]',
        'dvc[s3]',
        'pandas',
        'scikit-learn'
    ]
)