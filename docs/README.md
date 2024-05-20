# Documentation generation with Sphinx

This folder has the configuration necessary to generate the documentation of the Python code base in the source code. It used the
[Sphinx documentation generator](https://www.sphinx-doc.org/en/master/).


## Building the documentation

To build in production mode, use:

```shell
make production
```

If you want to build in development mode, use:

```
make development
```

If you only want to build one mode, use:

```
make <module_name>
```

Example:

```
make html
```

Note: this method will build the module in development mode.


### Cleaning the build directory

Use `make clean` to clean the build files.


## Other information

You can use `make help` to see the list of available `sphinx-build` commands and `make coverage` to see the
[coverage report](https://www.sphinx-doc.org/en/master/usage/extensions/coverage.html).


## Custom Field lists

In the docstrings of the source code you can add these extra field lists:

```python
"""
:issue:`1234` -> Shows the issue 1234 in the generated documentation (creates a hyperlink).
:pull:`1234` -> Shows the pull request 1234 in the generated documentation (creates a hyperlink).
"""
```
