#!/usr/bin/python3
"""class that locks creation of dynamic attributes
    unless it's called first_name"""


class LockedClass:
    """a locked class"""
    __slots__ = ["first_name"]
