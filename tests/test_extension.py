"""Tests for the `extension` module."""

from __future__ import annotations

from textwrap import dedent

import pytest
from griffe import DocstringAdmonition, DocstringSectionAdmonition, load_extensions, temporary_visited_module

from griffe_warnings_deprecated.extension import WarningsDeprecatedExtension


@pytest.mark.parametrize(
    "code",
    [
        """
        @warnings.deprecated("message", category=DeprecationWarning)
        def hello(): ...
        """,
        """
        @warnings.deprecated("message")
        def hello(): ...
        """,
        """
        @warnings.deprecated(
            "message",
            category=DeprecationWarning,
        )
        def hello(): ...
        """,
        """
        @warnings.deprecated(
            "mes"
            "sage",
            category=DeprecationWarning,
        )
        def hello(): ...
        """,
        """
        @warnings.deprecated(f"message", category=DeprecationWarning)
        def hello(): ...
        """,
        """
        @warnings.deprecated("message", category=DeprecationWarning)
        def hello():
            '''Summary.'''
        """,
        """

        @warnings.deprecated("message", category=DeprecationWarning)
        def hello():
            '''Summary.

            Description.
            '''
        """,
        """
        @warnings.deprecated("message", category=DeprecationWarning)
        def hello():
            '''Summary.

            Description.

            Note:
                Hello.
            '''
        """,
        """
        @warnings.deprecated("message", category=DeprecationWarning)
        class hello: ...
        """,
    ],
)
def test_extension(code: str) -> None:
    """Test the extension.

    Parameters:
        code: Code to test (parametrized).
    """
    code = f"import warnings\n{dedent(code)}"
    with temporary_visited_module(code, extensions=load_extensions(WarningsDeprecatedExtension)) as module:
        adm = module["hello"].docstring.parsed[0]
    assert isinstance(adm, DocstringSectionAdmonition)
    assert isinstance(adm.value, DocstringAdmonition)
    assert adm.title == "Deprecated"
    assert adm.value.kind == "danger"
    assert adm.value.contents == "message"
