from setuptools import setup, find_packages

with open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="flask-rapid",
    version="0.0.0",
    description="Flask framework enhancements for rapid and robust web API development.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/mobiusbyte/flask-rapid",
    project_urls={
        "Code": "https://github.com/mobiusbyte/flask-rapid",
        "Issue tracker": "https://github.com/mobiusbyte/flask-rapid/issues",
    },
    license="MIT",
    author="Jill San Luis",
    author_email="jill@mobiusbyte.com",
    packages=find_packages(),
    entry_points={},
    include_package_data=True,
    install_requires=[],
    extras_require={},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.7",
)
