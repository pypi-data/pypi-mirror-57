# -*- coding: utf-8 -*-

"""
Defines utilities pertaining to memoization processes
"""

__all__ = ["Memoized", 
           "SimpleMemoized",
           ]

import collections
import functools

class Memoized(object):
    """ Decorator
    
    Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned (not reevaluated).
    Source: https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
    
    Arguments:
        func: callable; the function to wrap, so that its output values be cached. If an input to 
            this function cannot be hashed, then the corresponding value will not be cached
    
    Attributes:
        func: callable; the function to wrap, so that its output values be cached. If an input to 
            this function cannot be hashed, then the corresponding value will not be cached
        
        cache: an "args => cached value" map, storing the cached value of the function
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # Uncacheable (a list, for instance); better not to cache than blow up.
            return self.func(*args)
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]
    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__
    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)

class SimpleMemoized(object):
    """ Decorator
    
    Caches a function's return value each time it is called, for a function that takes no argument.
    If called later, the cached value is returned (not reevaluated).
    
    Arguments:
        func: callable; the function to wrap (that take no argument) so that its output value be cached
    
    Attributes:
        func: callable; the function to wrap (that take no argument) so that its output value be cached
        
        cache: the cached value; is equal to None if the wrapped function has not been called yet
    """
    def __init__(self, func):
        self.func = func
        self.cache = None
    def __call__(self):
        if not self.cache:
            self.cache = self.func()
        return self.cache
    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__
    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)