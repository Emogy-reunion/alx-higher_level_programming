#!/usr/bin/python3
"""class that locks creation of dynamic attributes"""


class LockedClass:
    """a locked class"""
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        """locks the class"""
        if name != 'first_name':
            raise AttributeError(f"{self.__class__.__name__} has no attribute '{name}'")
        super().__setattr__(name, value)
