from spydrnet.ir.element import Element as ElementBase


class Element(ElementBase):
    ''' This class extends the default Element class '''

    @property
    def get_index(self):
        ''' Returns python index of element '''
        return self._bundle().get_index(self)

    @property
    def get_verilog_index(self):
        ''' Returns verilog index of element '''
        return self._bundle().get_verilog_index(self)

    def _bundle(self):
        """
        this function must be overridden in classes which returns bundle object
        Port or Cable
        """
        raise NotImplementedError
