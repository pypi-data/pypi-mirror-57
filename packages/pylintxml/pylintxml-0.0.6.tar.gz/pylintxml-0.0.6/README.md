## What is pylintxml?

pylintxml is a simple tool that allows creating simple xml 'linters'.

# Installation

The best way is to get the pip package management tool (or use a virtualenv)
and run the following:

`pip install pylintxml`

## Examples

Check out pylintxml\examples folder

Examples:

- `cd examples\qt && pylintxml sample.xml`
- `cd examples\qt && pylintxml sample.xml -s`
- `cd examples\qt && pylintxml sample.xml -s -v`
- `cd examples && pylintxml -r books\.lintxml books\sample.xml -s`
- `cd examples\books && pylintxml sample.xml -v`

## Usage

`pylintxml --help`
