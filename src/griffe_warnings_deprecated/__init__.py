"""griffe-warnings-deprecated package.

Griffe extension for `@warnings.deprecated` (PEP 702).
"""

from __future__ import annotations

from griffe_warnings_deprecated.extension import WarningsDeprecatedExtension

__all__: list[str] = ["WarningsDeprecatedExtension"]
