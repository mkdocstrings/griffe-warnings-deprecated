"""Deprecated. Import from `griffe_warnings_deprecated` directly."""

# YORE: Bump 2: Remove file.

import warnings
from typing import Any

from griffe_warnings_deprecated._internal import extension


def __getattr__(name: str) -> Any:
    warnings.warn(
        "Importing from `griffe_warnings_deprecated.extension` is deprecated. "
        "Import from `griffe_warnings_deprecated` directly.",
        DeprecationWarning,
        stacklevel=2,
    )
    return getattr(extension, name)
