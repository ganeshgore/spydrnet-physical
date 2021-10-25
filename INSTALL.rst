.. _INSTALL.rst:

Install
=======

*SpyDrNet-Physical* is a plugin for `SpyDrNet <https://github.com/byuccl/spydrnet>`_ project, which adds functionality to perform physical design-related netlist transformations.

Installation
------------

Run one of the following commands to install the latest release of *SpyDrNet-Physical*.


.. code-block:: bash

   python3 -m pip install spydrnet-physical # For global installation or
   python3 -m pip install spydrnet-physical --user #  For local installation or
   # To install from git repo instead of pip
   python3 -m pip install git+https://github.com/ganeshgore/
   spydrnet_physical#latest

To install a current bleeding edge (under development) version directly from GitHub


.. code-block:: bash

   pip install git+https://github.com/ganeshgore/spydrnet_physical


.. note:: Installing SpyDrNet-Physical module will install SpyDrNet package. For more detailed information related to SpyDrNet installation, please visit.


Dependencies
------------

`SpyDrNet-Physical` depends on the following packages for functionality like rendering in browser and exporting SVG file.
- `websock <https://pypi.org/project/websock/>`_ To create a WebSocket connect with a browser
- `svgwrite <https://pypi.org/project/svgwrite/>`_ To render netlist in SVG
