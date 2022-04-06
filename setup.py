import pathlib
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Software Development :: Libraries",
]

requirements = []

test_requirements = ["codecov", "coverage", "pytest", "pytest-cov"]

main = pathlib.Path(__file__).parent
about = {}
with open(main / "dupeutil" / "__version__.py", "r", encoding="utf-8") as f:
    exec(f.read(), about)

setuptools.setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=setuptools.find_packages(include=["dupeutil"], exclude=["ext"]),
    package_data={"": ["LICENSE"]},
    package_dir={"dupeutil": "dupeutil"},
    include_package_data=True,
    python_requires=">=3.6, <4",
    install_requires=requirements,
    license=about["__license__"],
    zip_safe=False,
    classifiers=classifiers,
    keywords=["duplicate", "files", "commandline", "dupeutil"],
    tests_require=test_requirements,
    project_urls={"Source": "https://github.com/giosali/dupeutil"},
    entry_points={"console_scripts": ["dupeutil=dupeutil.main:main"]},
)
