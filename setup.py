from setuptools import find_packages, setup

setup(
    name="django-crispy-bulma-redux",
    version="0.3",
    description="Bulma.io template pack for django-crispy-forms",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Christoph Krybus",
    author_email="ckrybus@googlemail.com",
    url="https://github.com/ckrybus/django-crispy-bulma",
    license="MIT",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=["Django>=2.2", "django-crispy-forms>=1.9.0"],
    python_requires=">=3.6",
    include_package_data=True,
    zip_safe=False,
)
