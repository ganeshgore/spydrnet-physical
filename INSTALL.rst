.. _INSTALL.rst:

Install
=======

Run one of the following commands to install the latest release of *SpyDrNet-Physical*.


.. code-block:: bash

   # We have not released spydrnet-physical package to pip yet
   # Once the library is released you can use the following commands to install the package
   # python3 -m pip install spydrnet-physical # For global installation or
   # python3 -m pip install spydrnet-physical --user #  For local installation or
   # 
   # Meanwhile, to install from a git repo, run the following command 
   python3 -m pip install git+https://github.com/ganeshgore/spydrnet-physical.git

To install a current bleeding edge (current;y under development) version directly from GitHub


.. code-block:: bash

   pip install git+https://github.com/ganeshgore/spydrnet_physical@pre_release


.. note:: Installing ``SpyDrNet-Physical`` module will install SpyDrNet package. For more detailed information related to SpyDrNet installation, please visit.


Dependencies
------------

`SpyDrNet-Physical` depends on the following packages for functionality like rendering in browser and exporting SVG file.
- `websock <https://pypi.org/project/websock/>`_ To create a WebSocket connect with a browser
- `svgwrite <https://pypi.org/project/svgwrite/>`_ To render netlist in SVG
