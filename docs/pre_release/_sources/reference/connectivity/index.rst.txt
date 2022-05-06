'''''''''''''''''''''''''''''''
Connectivity Pattern Generation
'''''''''''''''''''''''''''''''

Floorplanning of a grid-based design requires careful planning of the 
global signal, as it significantly affects the physical design 
decisions such as the channel spacing, pin placement,
pin placement congestion etc.
The utility classes provided here provide a sophisticated way
to design global signal connectivity. 
We make assumptions that a design can be represented as a grid, 
and each index on the top level can be mapped to each (x,y) coordinate, 
as shown in the following figure.

.. figure:: ../figures/clock_grid.svg
    :width: 300px
    :align: center

    Base Grid


The connectivity pattern generated here creates 
a set of connection points (ConnectPointList)
which indicates the top-level connections between top instances.
For Example above figure shows that the global net is connected to 
the bottom port of the instance `(3,1)`. The feedthrough from the instance `(3,1)` 
outputs signal to top output port, which is connected to the bottom input of the 
instance `(3,2)`.

The grid allowed to `(1,1)` coordinate, 
any incoming/outgoing connection outside the grid is considered as 
a top-level connection. 

.. note:: These classes only allow horizontal or vertical connection; a diagonal connection is not legal


:doc:`ConnectionPattern <../utility_classes/ConnectionPattern>`
................................................

This is a primary grid that creates different connection patterns 
like H-tree structure, fish-bone structure, etc.


:doc:`ConnectPointList <../utility_classes/ConnectPointList>`
................................................
This class holds the list of connection points (ConnectPoint) 
and enables matrix operations like rotate, move_x, move_y, etc.
Creating multiple ConnectPointList and merging them allows
for more complex pattern creation.


:doc:`ConnectPoint <../utility_classes/ConnectPoint>`
................................................
This class stores the properties of the connection between two instances.


Examples:
.........

Please refer `exmaples <sec:clock_tree_embedding>`_ section to learn more