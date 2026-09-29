# SPDX-License-Identifier: ISC
#
# ISC License
#
# Copyright (c) 2023, Timothée Mazzucotelli and contributors
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# Griffe extension for `@warnings.deprecated` (PEP 702).

from __future__ import annotations

import ast
from typing import Any

from griffe import Class, Docstring, DocstringSectionAdmonition, ExprCall, Extension, Function, get_logger

_logger = get_logger(__name__)
_self_namespace = "griffe_warnings_deprecated"
_mkdocstrings_namespace = "mkdocstrings"
_decorators = {"warnings.deprecated", "typing_extensions.deprecated"}


def _deprecated(obj: Class | Function) -> str | None:
    for decorator in obj.decorators:
        if decorator.callable_path in _decorators and isinstance(decorator.value, ExprCall):
            first_arg = decorator.value.arguments[0]
            try:
                return ast.literal_eval(first_arg)  # ty:ignore[invalid-argument-type]
            except ValueError:
                _logger.debug("%s is not a static string", str(first_arg))
                return None
    return None


class WarningsDeprecatedExtension(Extension):
    """Griffe extension for `@warnings.deprecated` (PEP 702)."""

    def __init__(
        self,
        kind: str = "danger",
        title: str | None = "Deprecated",
        label: str | None = "deprecated",
    ) -> None:
        """Initialize the extension.

        Parameters:
            kind: Admonitions kind.
            title: Admonitions title.
            label: Label added to deprecated objects.
        """
        super().__init__()
        self.kind = kind
        """The kind of the admonition to insert in the docstring."""
        self.title = title or ""
        """The title of the admonition to insert in the docstring."""
        self.label = label
        """The label added to deprecated objects."""

    def _insert_message(self, obj: Function | Class, message: str) -> None:
        title = self.title
        if not self.title:
            title, message = message, title
        if not obj.docstring:
            obj.docstring = Docstring("", parent=obj)
        sections = obj.docstring.parsed
        sections.insert(0, DocstringSectionAdmonition(kind=self.kind, text=message, title=title))

    def on_class_instance(self, *, cls: Class, **kwargs: Any) -> None:  # noqa: ARG002
        """Add section to docstrings of deprecated classes."""
        if message := _deprecated(cls):
            cls.deprecated = message
            self._insert_message(cls, message)
            if self.label:
                cls.labels.add(self.label)

    def on_function_instance(self, *, func: Function, **kwargs: Any) -> None:  # noqa: ARG002
        """Add section to docstrings of deprecated functions."""
        if message := _deprecated(func):
            func.deprecated = message
            self._insert_message(func, message)
            if self.label:
                func.labels.add(self.label)
