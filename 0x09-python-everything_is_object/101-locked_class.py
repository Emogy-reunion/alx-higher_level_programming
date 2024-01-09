#!/usr/bin/python3

class LockedClass:
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(f"{self.__class__.__name__} has no attribute '{name}'")
        super().__setattr__(name, value)
