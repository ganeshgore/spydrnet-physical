
Tutorial
========

This tutorial focuses on hierarchical physical restructuring using ``spydrnet-physical`` plugin.
If you are starting with a ``spydrnet`` project and looking for complete detail 
of the data structure and base classes of ``SpyDrNet`` please refer
`byuccl/SpyDrNet Documentation <https://byuccl.github.io/spydrnet/docs/stable/index.html>`_. 
This tutorial focuses mainly on reading the existing Verilog netlist in spydrnet
project and performing a series of netlist manipulation (which are correct by construction) to 
achieve the intended netlist structure.

.. Note:: SpyDeNet focuses only on restructural Verilog netlist, netlists containing
        always and initial blocks are not valid structure netlists.


.. toctree::
    :hidden:

    Example <?http://#example>
    Shell Interface <?http://#shell-interface>
    Visualization <?http://#visualization>


Example
-------

The following example shows how you can perform a netlist manipulation. 
In this example, we are going to generate feedthrough for a single wire
connected between `in0` input port and `in1` port of instance `inst_1__1`.
The cable/net name of this connection is `wire0`, which is obtained from the 
the Verilog netlist :ref:`sample_verilog_basic_hierarchy`
(`wire name is not annotated in the following schematic`).

.. image:: ../auto_sample_verilog/basic_hierarchy.svg
    :align: center

.. code-block:: python

    from os import path
    import spydrnet as sdn
    import spydrnet_physical as sdnphy

    netlist = sdnphy.load_netlist_by_name('basic_hierarchy')
    
    # Read example netlist
    top = netlist.top_instance.reference

    # get instance of wire0 and inst_2_0
    cable0 = next(top.get_cables("wire0"))
    inst2 = next(top.get_instances("inst_1_0"))
    top.create_feedthrough(inst2, cable0)

    # Add dummy unconnected wire
    top.create_unconn_wires()
    sdn.compose(netlist, '_output_wire.v', skip_constraints=True)

Output
^^^^^^

.. hdl-diagram:: ../../../examples/basic/_output_wire.v
   :type: netlistsvg
   :align: center
   :module: top


*For more detail of spydrnet-physical features and examples, please check* `<examples>`_ *section*


.. _sdn_phy_shell::
Shell Interface
---------------

``SpyDrNet-Physical`` allows you to load a shell-like interface after
to perform live modifications and debugging of the Script.

A shell like interactive interface can be involked by running ``sdnphy`` command
which opens interactive shell enviroment as shown below.

.. code-block:: 

    bash>>> sdnphy

     ___           ___      _  _     _       ___ _           _         _ 
    / __|_ __ _  _|   \ _ _| \| |___| |_ ___| _ \ |_ _  _ __(_)__ __ _| |
    \__ \ '_ \ || | |) | '_| .` / -_)  _|___|  _/ ' \ || (_-< / _/ _` | |
    |___/ .__/\_, |___/|_| |_|\_\___|\__|   |_| |_||_\_, /__/_\__\__,_|_|
        |_|   |__/                                   |__/                
        
    Launching SpyDrNet-Physical interactive mode
     
    spydrnet >>>


In-script debugging
^^^^^^^^^^^^^^^^^^^^

A shell-like interface can also be invoked from the python script. Use the 
following command to import shell and launch.

.. code-block:: python 

    from spydrnet_physical.utils.shell import launch_shell

    # 
    # script before launching the shell
    #
    launch_shell()
    #
    # script after exiting the shell
    #


For more information related to shell interface and shortcuts, please read 
:ref:`sdnphy Shell <sdn_phy_shell>` section.


Visualization
-------------

Spydrnet-physical also provides a basic hierarchical visualizer based on 
project project `Nic30/d3-hwschematic <https://github.com/Nic30/d3-hwschematic>`_.
The following example script can be used to export an HTML file to visualize live 
on the web browser.

.. code-block:: python

    import spydrnet_physical as sdnphy
    from spydrnet_physical.composers.html.composer import HTMLComposer

    netlist = sdnphy.load_netlist_by_name('basic_hierarchy')

    composer = HTMLComposer()
    composer.run(netlist, file_out="_initial_design.html")

.. Note:: Due to the Cross-Origin Resource Sharing policy, the HTML page can not be embedded 
    on this page. To visualize the netlist, please click on the following link.

`Open schematic in separate window </_images/_initial_design.html>`_