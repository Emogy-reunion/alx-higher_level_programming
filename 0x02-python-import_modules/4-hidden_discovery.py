#!/usr/bin/python3

if __name__ == "__main__":
    """
    Print all names defined in the compiled hidden_4 module.
    """
    import hidden_4

    _names = dir(hidden_4)
    for _name in _names:
        if _name[:2] != "__":
            print(_name)
