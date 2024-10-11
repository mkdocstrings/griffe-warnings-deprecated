---
hide:
- feedback
---

--8<-- "README.md"

## Examples

### Normal admonition

Given the following code:

```python exec="1" result="python"
print('--8<-- "docs/examples/normal.py"')
```

And this *mkdocstrings* configuration:

```md exec="1" source="above"
Here is the rendered HTML:  <!-- markdown-exec: hide -->

::: normal.function
    options:
      heading_level: 4
      extensions: [griffe_warnings_deprecated]

::: normal.other_function
    options:
      heading_level: 4
```

### Admonition with message as title

Given the following code:

```python exec="1" result="python"
print('--8<-- "docs/examples/notitle.py"')
```

And this *mkdocstrings* configuration:

```md exec="1" source="above"
Here is the rendered HTML:  <!-- markdown-exec: hide -->

::: notitle.function
    options:
      heading_level: 4
      extensions:
      - griffe_warnings_deprecated:
          title: null
          kind: warning
```