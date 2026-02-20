# normal.py
import warnings


@warnings.deprecated(
    "This function is deprecated, use [`other_function`][normal.other_function] instead.",
    category=DeprecationWarning,
)
def function() -> int:
    """Do something.

    Do something in a suboptimal manner.

    Returns:
        An integer.
    """
    return 0


def other_function() -> int:
    """Do something.

    Do something in an optimal manner.

    Returns:
        An integer.
    """
    return 1
