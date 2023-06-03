# coverage-python-example
Simple example of using Python's `coverage` package with a simple Python module.

## Commands

* `coverage run one_statement_over_several_lines.py`
* `coverage run miss_one_of_sixteen_lines.py`
* `coverage run miss_thirteen_of_sixteen_lines.py`
* `coverage report`
* `coverage html`

## Notes

* It seems that coverage counts the `if` statement as a line of code even if the enclosing block is not executed. This is because the `if` statement has to execute in order to determine if the enclosed block needs to execute or not.
* `coverage` measures the number of lines executed when the code is executed, not the number of lines which are 'tested'.
* If a Python 'statement' is spready over several lines of code, `coverage` counts it as one statement.

## PyPI Packages

* <https://pypi.org/project/coverage/>
