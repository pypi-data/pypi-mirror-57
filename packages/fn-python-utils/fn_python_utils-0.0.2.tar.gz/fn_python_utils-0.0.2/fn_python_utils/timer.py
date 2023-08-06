# -*- coding: utf-8 -*-

"""
Defines utilities pertaining to the measuring of a callable's execution duration
"""

__all__ = ["timer", 
           "format_seconds_nb",
           ]

import functools
import time
import numpy as np


def timer(display_fct=print, message=None, decimals=2):
    """ Creates a wrapper that can be used to wrap a function in order to create a wrapped function, 
    one that measures the duration of execution of the initial function, and passes messages to the 
    input 'display_fct' before and after the wrapped function's execution, as well as a message 
    providing the measured duration.
    
    Args:
        display_fct: callable that must take a string as an input
        message: a string, a pair of string, or None; if a pair, then the first will be used for 
            the message to be displayed just before the beginning of the execution of the wrapped function, 
            whereas the second will be used for the message to be displayed just after; if a string, will 
            be used both for the beginning and the end; if None, the name of the function will be used.
        decimals: int, default is 2; number of decimal to use when displaying the function's 
            execution duration (in seconds).

    Returns:
        callable, a wrapper function
    """
    if message is None:
        begin_message_fct = lambda func: str(func.__name__)
        end_message_fct = lambda func: str(func.__name__)
    elif isinstance(message, str):
        begin_message_fct = lambda func: message
        end_message_fct = lambda func: message
    elif isinstance(message, tuple):
        begin_message_fct = lambda func: str(message[0])
        end_message_fct = lambda func: str(message[1])
    else:
        raise NotImplemented("message input type = '{}'".fotmat(type(message)))
    
    def create_timed_function(func):
        """ Wraps a function so as to display a message just before and just after the execution of 
        the function, a well as to measure the duration of its execution.
            func: callable, function to be wrapped

        Returns:
            the wrapped function
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            display_fct("Starting {} ...".format(begin_message_fct(func)))
            start_time = time.time()
            response = func(*args, **kwargs)
            end_time = time.time()
            display_fct("Finished {}.".format(end_message_fct (func)))
            duration = end_time - start_time
            display_fct("Duration: {}".format(format_seconds_nb(duration, decimals=decimals)))
            return response
        return wrapper

    return create_timed_function

def format_seconds_nb(seconds_nb, decimals=-1):
    """ Formats a time duration (expressed in seconds) into a human-readable string.
    
    Args:
        seconds_nb: float, duration expressed in seconds
        decimals: number of decimals to consider using for the string representation of the duration

    Returns:
        string
    """
    if seconds_nb is None:
        a_string = ""
    elif np.isnan(seconds_nb):
        a_string = "NaNs"
    else:
        the_sign = np.sign(seconds_nb)
        used_duration = the_sign*seconds_nb
        if (decimals > -1):
            decimals = int(decimals)
            used_duration = np.around(used_duration, decimals)
        
        date_keys_list = [["C",100*365.4*24*60*60],["Y",365.25*24*60*60],["M",30.5*24*60*60],["D",24*60*60],["h",60*60],["m",60],["s",1]]
        str_array = []
        remaining_secs_nb = int(used_duration)
        if used_duration > 0:
            for symb, nb_secs in date_keys_list:
                nb_symb, remaining_secs_nb = divmod(remaining_secs_nb, nb_secs)
                if nb_symb > 0:
                    to_add = "{:s}{:s}".format(str(int(the_sign*nb_symb)), symb)
                    str_array.append(to_add)
            ms_nb = 1000 * np.around(used_duration-int(used_duration), 3)
            μs_nb = 1000000 * np.around(used_duration-(int(used_duration)+ms_nb/1000), 6)
            if ms_nb > 0 or μs_nb > 0:
                if ms_nb>0:
                    a_nb = ms_nb
                    to_add = "{:d}ms".format(int(the_sign*a_nb))
                    str_array.append(to_add)
                if μs_nb>0:
                    a_nb = μs_nb
                    to_add = "{:d}μs".format(int(the_sign*a_nb))
                    str_array.append(to_add)
            else:
                μs_nb = np.around(1000000*(used_duration - int(used_duration)), 0)
                a_nb = μs_nb
                to_add = "{:s}μs".format(str(int(the_sign*a_nb)))
                str_array.append(to_add)
        else:
            to_add = "0s"
            str_array.append(to_add)
        a_string = " ".join(str_array)
    
    return a_string
