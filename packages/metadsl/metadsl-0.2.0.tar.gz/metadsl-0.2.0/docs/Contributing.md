# Contributing

## Development

Either use repo2docker:

```bash
repo2docker -E .
```

Or get started with Conda/flit:

```bash
conda create -n metadsl jupyterlab llvmlite
conda activate metadsl
pip install flit
flit -f typez.pyproject.toml install --symlink
flit install --symlink
flit -f core.pyproject.toml install --symlink
flit -f visualize.pyproject.toml install --symlink
flit -f llvm.pyproject.toml install --symlink

# optional
jupyter labextension install ./typez
```

### Tests

This runs mypy and tests, and reports coverage.

```bash
pytest --cov --mypy
# open coverage file
open htmlcov/index.html
```

You can also test that the documentation notebooks run correctly, but this
[must be run separately from the code coverage](https://github.com/computationalmodelling/nbval/issues/116):

```bash
pytest docs/*.ipynb --nbval
```

### Debugging

If you have a notebook that isn't working, one way to debug it is to convert it to a Python
script, and then run that python script with `pudb`.

```bash
jupyter nbconvert --to script Notebook.ipynb
python -m pudb Notebook.py
```

### Docs

```bash
sphinx-autobuild docs docs/_build/html/
```
