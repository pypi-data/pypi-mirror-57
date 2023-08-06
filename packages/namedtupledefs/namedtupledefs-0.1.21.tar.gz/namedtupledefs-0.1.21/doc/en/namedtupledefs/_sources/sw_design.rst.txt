
.. _SWDESIGN:

The SW-Design of *namedtupledefs*
*********************************

Changes to the original code extracted from standard library *collections*:

#. The template for the created tuple class:
   
   #. Added member variable _fielddefaults - for documentation and online use.
    
   #. Changed the call parameters of __new__ to {new_args} - with default values.

   #.  Added method *_merge*

#. The fabric code - *namedtuple* function:
   
   #. Added documentation in functions doc-string. 
   
   #. Added code block for the creation of the call argument string of '__new__'.
    
   #. Added 'new_args' and '_fielddefaults' to the format parameters of the class template. 


