.. _INSTALL.rst:

Install
========

Run one of the following commands to install the latest release of *SpyDrNet-Physical*.


.. code-block:: bash

   # We have not released spydrnet-physical package to pip yet
   # Once the library is released, you can use the following commands to install the package
   # python3 -m pip install spydrnet-physical # For global installation or
   # python3 -m pip install spydrnet-physical --user #  For local installation or
   # 
   # Meanwhile, to install from a git repo, run the following command 
   python3 -m pip install git+https://github.com/ganeshgore/spydrnet-physical.git


Development Version
-------------------

To install a current bleeding edge (current;y under development) version directly from GitHub


.. code-block:: bash

   pip install git+https://github.com/ganeshgore/spydrnet_physical@pre_release


.. note:: Installing ``SpyDrNet-Physical`` module will install ``SpyDrNet`` package. 
   For more detailed information related to SpyDrNet installation, please visit.


Validate Installation
----------------------

To enable plugins while using ``Spydrnet``, please create `.spydrnet` file 
in your home directory. This file contains the list of plugins to load while 
loading ``spydrnet`` library. To enable ``spydrnet_physical``, 
add ``spydrnet_physical`` in the `.spydrnet` file. 
Alternately run the  following command 

.. code-block:: bash

   echo "spydrnet_physical" > .spydrnet

To check if the ``spydrnet_physical`` plugin loads correctly, execute

.. code-block:: bash

   python3 -c "import spydrnet as sdn;print(sdn.get_active_plugins().keys())"
   # Expected output:
   # dict_keys(['spydrnet_physical'])


Dependencies
------------

`SpyDrNet-Physical` depends on the following packages for functionality like rendering in browser and exporting SVG file.

- `websock <https://pypi.org/project/websock/>`_ To create a WebSocket connect with a browser
- `svgwrite <https://pypi.org/project/svgwrite/>`_ To render netlist in SVG
