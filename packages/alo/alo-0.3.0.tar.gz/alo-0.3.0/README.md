# alo

[![](https://img.shields.io/pypi/v/alo.svg)](https://pypi.python.org/pypi/alo)
[![](https://img.shields.io/travis/uchuhimo/alo.svg)](https://travis-ci.org/uchuhimo/alo)
[![](https://github.com/uchuhimo/alo/workflows/Python%20package/badge.svg)](https://github.com/uchuhimo/alo/actions)
[![Documentation Status](https://readthedocs.org/projects/alo/badge/?version=latest)](https://alo.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/uchuhimo/alo/shield.svg)](https://pyup.io/repos/github/uchuhimo/alo/)

A tool to combine function with DAG.

- Documentation: https://alo.readthedocs.io.

## Development

### Create a virtual environment

```bash
conda env create -f environment.yml
source activate alo
```

### Install dependencies

There are two options:

- Use poetry:
    ```bash
    poetry install
    ```
- Use pip:
    ```bash
    pip install -e ".[dev]"
    ```

### Update dependencies

```bash
poetry update
```

### Bump version

```bash
bumpversion minor  # major, minor, patch
```

### Show information about installed packages

```bash
poetry show
```

### Show dependency tree

```bash
dephell deps tree
# or
dephell deps tree pytest
```

### Install git pre-commit hooks

```bash
pre-commit install
```

# License

© uchuhimo, 2019. Licensed under an [Apache 2.0](./LICENSE) license.
