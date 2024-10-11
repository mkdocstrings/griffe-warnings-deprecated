# griffe-warnings-deprecated

[![ci](https://github.com/mkdocstrings/griffe-warnings-deprecated/workflows/ci/badge.svg)](https://github.com/mkdocstrings/griffe-warnings-deprecated/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs-708FCC.svg?style=flat)](https://mkdocstrings.github.io/griffe-warnings-deprecated/)
[![pypi version](https://img.shields.io/pypi/v/griffe-warnings-deprecated.svg)](https://pypi.org/project/griffe-warnings-deprecated/)
[![gitpod](https://img.shields.io/badge/gitpod-workspace-708FCC.svg?style=flat)](https://gitpod.io/#https://github.com/mkdocstrings/griffe-warnings-deprecated)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://app.gitter.im/#/room/#griffe-warnings-deprecated:gitter.im)

Griffe extension for `@warnings.deprecated`
([PEP 702](https://peps.python.org/pep-0702/)).

## Installation

```bash
pip install griffe-warnings-deprecated
```

## Usage

The option values in the following examples are the default ones,
you can omit them if you like the defaults.

### Command-line

```bash
griffe dump mypackage -e griffe_warnings_deprecated
```

See [command-line usage in Griffe's documentation](https://mkdocstrings.github.io/griffe/extensions/#on-the-command-line).

### Python

```python
import griffe

griffe.load(
    "mypackage",
    extensions=griffe.load_extensions(
        [{"griffe_warnings_deprecated": {
            "kind": "danger",
            "title": "Deprecated",
            "label": "deprecated"
        }}]
    )
)
```

See [programmatic usage in Griffe's documentation](https://mkdocstrings.github.io/griffe/extensions/#programmatically).

### MkDocs

```yaml title="mkdocs.yml"
plugins:
- mkdocstrings:
    handlers:
      python:
        options:
          extensions:
          - griffe_warnings_deprecated:
              kind: danger
              title: Deprecated
```

See [MkDocs usage in Griffe's documentation](https://mkdocstrings.github.io/griffe/extensions/#in-mkdocs).

---

Options:

- `kind`: The admonition kind (default: danger).
- `title`: The admonition title (default: Deprecated).
    Can be set to null to use the message as title.
- `label`: The label added to deprecated objects (default: deprecated).
    Can be set to null.
