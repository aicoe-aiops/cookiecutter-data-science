"""Package manifest for this template repo."""

from setuptools import find_packages, setup

__version__ = "0.1.0"

setup(
    name="src",
    packages=find_packages(),
    version=__version__,
    description="{{ cookiecutter.description }}",
    author="{{ cookiecutter.author_name }}",
{%- if cookiecutter.open_source_license == "MIT" %}
    license="MIT",
{% elif cookiecutter.open_source_license == "BSD-3-Clause" %}
    license="BSD-3",
{% else %}
    license="",
{% endif -%}
)
