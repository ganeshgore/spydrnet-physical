import typing
from spydrnet.ir.first_class_element import FirstClassElement as FirstClassElementBase


if typing.TYPE_CHECKING:
    from spydrnet.ir.first_class_element import FirstClassElement as FirstClassElementSDN
    from spydrnet_physical.ir.element import Element as ElementPhy
    FirstClassElementBase = type(
        "FirstClassElementBase", (FirstClassElementSDN, ElementPhy), {})


class FirstClassElement(FirstClassElementBase):
    ''' Extends the base first FirstClassElement'''

    def somhing(self):
        print(self.get_verilog_index)

    @property
    def properties(self):
        """
        Returns properties of the object

        ``spydrnet-physical`` considers properties defined in the
        verilog netlist are physical design related

        """
        try:
            return self.data["VERILOG.InlineConstraints"]
        except KeyError:
            self._data["VERILOG.InlineConstraints"] = dict()
            return self.data["VERILOG.InlineConstraints"]
