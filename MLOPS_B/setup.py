import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"


REPO_NAME = "MLOPS_B"
AUTHOR_USERNAME = "franklinobasy"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "franklinobasy@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/MlOps-Projects/tree/main/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/MlOps-Projects/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
