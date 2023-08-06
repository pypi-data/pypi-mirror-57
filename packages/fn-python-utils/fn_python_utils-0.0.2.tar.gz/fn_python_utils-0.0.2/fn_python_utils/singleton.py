# -*- coding: utf-8 -*-


"""
Defines a Singleton class
"""

__all__ = ["Singleton",
           ]

class Singleton(object):
    """ Each class that inherit from this class will adopt a Singleton behavior. That is, when 
    creating an instance of the child class, if an instance of this class already exist, then it is 
    this instance that will be returned, and not a new instance.    
    """
    _INSTANCES = {}
    def __new__(cls, *args, **kwargs):
        if cls not in cls._INSTANCES:
            cls._INSTANCES[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._INSTANCES[cls]
