from spydrnet.ir.first_class_element import FirstClassElement as FirstClassElementBase


class FirstClassElement(FirstClassElementBase):
    ''' Extends the base first FirstClassElement'''

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
