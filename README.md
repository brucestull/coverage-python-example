# coverage-python-example
Simple example of using Python's `coverage` package with a simple Python module.

## Commands

* `coverage run append_to_list.py`
* `coverage report`
* `coverage html`

## Notes

* It seems that coverage counts the `if` statement as a line of code even if the enclosing block is not executed. This is because the `if` statement has to execute in order to determine if the enclosed block needs to execute or not.

## PyPI Packages

* <https://pypi.org/project/coverage/>
