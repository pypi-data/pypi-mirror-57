# -*-coding:utf-8 -*

"""
Defines utilities pertaining to the display of information / useful for logging tasks
"""

__all__ = ["create_logged_iterator_wrapper", 
           "create_display_progress_function", 
           ]


import math

def create_logged_iterator_wrapper(
        function, percentage_interval=5, count_interval=1000, 
        personalized_progress_message=None):
    
    def logged_iterator(iterable):
        maximum_count = None
        try:
            maximum_count = len(iterable)
        except Exception as e:
            if not (e.args and isinstance(e.args[0], str) and e.args[0].endswith("has no len()")):
                raise
        
        display_progress_function =\
         create_display_progress_function(
             function, maximum_count=maximum_count, 
             percentage_interval=percentage_interval, count_interval=count_interval, 
             personalized_progress_message=personalized_progress_message)
        
        return create_logged_iterator(display_progress_function, iterable)
    
    return logged_iterator


def create_logged_iterator(display_progress_function, iterable):
    for i, val in enumerate(iter(iterable)):
        display_progress_function(i)
        yield val
    
def create_display_progress_function(
        function, maximum_count=None, percentage_interval=5, 
        count_interval=1000, personalized_progress_message=None):
    """ Creates a 'display function' to be used to log the progress of an iteration.
    
    The aim of this function is to create a 'display function' that shall 
    be called repeatedly along an iteration, so as to log its progress. 
    This 'display function' will expect to take a non-negative integer 'k' 
    as an input, which is supposed to represent the number of iterations which 
    have been completed when the 'display function' is being called (ex: 0, 1, 2...).
    
    This function is useful if you already know the number 'maximum_count' of step that 
    the iteration will necessitate: in this case, a percentage progress will 
    be displayed along the value of 'k', with the possibility to specify 
    the percentage interval to use (e.g.: 5% => display progress levels 
    corresponding to 0%, 5%, 10%, etc). The progress message will be sent 
    to the 'logger' specified, using the 'logging_level' log level value. 
    You have the possibility to pass along a personalized progress message 
    if you wish to. This personalized message must be a string ready to be 
    formated using the 'format' method of python 3, with the placeholders 
    such as demonstrated in the example below. 
    
    Parameters
    ----------
    function: callable
        The function that will be called by inputing a progress message, when appropriate.
    maximum_count: int
        Total size of the iteration whose progress we want to monitor. Needs to 
        be a positive integer if percentage progress is to be displayed.
    step: int
        If maximum_count is defined and positive, this is the percentage value 
        whose multiples will be displayed when the iteration reaches the 
        corresponding progress stage (their values will be comprised within 
        [0; 100)). If maximum_count is negative or not defined, this is the 
        integer interval between two progress display.
    personalized_progress_message: string
        Progress message to use.
        Ex: "Current progress = {percentage:6.2f}% ({current:d} / {total:d})"
    
    Returns
    -------
    callable:
        Function which takes an integer as an input, and calls the log function 
        when necessary.
    """
    
    if maximum_count is not None and maximum_count >= 1:
        used_percentage_interval = float(abs(percentage_interval))
        if used_percentage_interval == 0:
            used_percentage_interval = 1
        # k belongs to [0; maximum_count-1]; more interested in specifying that the progress has begun, that in specifying that it just ended.
        a_dict = _create_threshold_count2percentage_data(used_percentage_interval, maximum_count)
        
        l = len(str(maximum_count))
        message = "Current progress = {percentage:6.2f}% ({current:"+str(l)+"d} / {total:"+str(l)+"d})"
        if personalized_progress_message is not None:
            message = personalized_progress_message
        
        def display_message(k):
            if (k in a_dict):
                a_tuple = a_dict[k]
                function(message.format(percentage=a_tuple[0], current=a_tuple[1], total=a_tuple[2]))
        result = display_message
    
    else:
        used_count_interval = count_interval
        if used_count_interval is None or used_count_interval < 1:
            used_count_interval = 1000
        used_count_interval = int(used_count_interval)
        
        message = "Iteration n°{current:d}"
        if personalized_progress_message is not None:
            message = personalized_progress_message
        
        result = lambda k: function(message.format(current=k)) if k % used_count_interval == 0 else None
    
    return result

def create_perc_progress_message_format(maximum_nb, prefix=""):
    maximum_nb = int(maximum_nb)
    assert maximum_nb > 0
    l = len(str(maximum_nb))
    message =\
        "{percentage:6.2f}% ({current:"+str(l)+"d} / {total:"+str(l)+"d})"
    if prefix:
        message = "{}: {}".format(prefix, message)
    return message


class ProgressAcknowledger(object):

    def __init__(self, current_nb_input_fcts=None, accum_nb_input_fcts=None):
        current_nb_input_fcts =\
            tuple() if current_nb_input_fcts is None else tuple(current_nb_input_fcts)
        accum_nb_input_fcts =\
            tuple() if accum_nb_input_fcts is None else tuple(accum_nb_input_fcts)
        self._current_nb_input_fcts = current_nb_input_fcts
        self._accum_nb_input_fcts = accum_nb_input_fcts
        self._accum = 0
    
    def acknowledge(self, current_nb):
        for fct in self._current_nb_input_fcts:
            fct(current_nb)
        self._accum += current_nb
        for fct in self._accum_nb_input_fcts:
            fct(self._accum)

class PercAccumAcknowledger(object):

    def __init__(self, function, maximum_nb=None, percentage_interval=5, prefix=None):
        used_percentage_interval = float(abs(percentage_interval))
        if used_percentage_interval == 0:
            used_percentage_interval = 1
        # k belongs to [0; maximum_count-1]; more interested in specifying that the progress has begun, that in specifying that it just ended.
        threshold_nb2percentage_data =\
            _create_threshold_count2percentage_data(used_percentage_interval, maximum_nb)
        threshold_nbs = sorted(threshold_nb2percentage_data.keys(), reverse=True)
        
        message_format = create_perc_progress_message_format(maximum_nb, prefix=prefix)
        
        self.function = function
        self.maximum_nb = maximum_nb
        self.percentage_interval = percentage_interval
        self.message_format = message_format
        self._accum = 0
        self._threshold_nbs = threshold_nbs
        self._threshold_nb2percentage_data = threshold_nb2percentage_data
    
    def acknowledge(self, current_nb):
        self._accum += current_nb
        try:
            threshold_nb = self._threshold_nbs[-1]
        except IndexError:
            pass
        else:
            if self._accum >= threshold_nb:
                a_tuple = self._threshold_nb2percentage_data[threshold_nb]
                message = self.message_format.format(percentage=a_tuple[0], current=a_tuple[1], total=a_tuple[2])
                self.function(message)
                self._threshold_nbs.pop()




def _create_threshold_count2percentage_data(percentage_interval, maximum_count):
    threshold_count2percentage_data = {}
    max_multiplier_integer = int(math.floor(100. / percentage_interval))
    for multiplier_integer in range(max_multiplier_integer+1):
        percentage_value = percentage_interval * multiplier_integer
        threshold_count = int(-math.floor(-maximum_count * percentage_value / 100.))
        threshold_count2percentage_data[threshold_count] = (percentage_value, threshold_count, maximum_count)
    return threshold_count2percentage_data
