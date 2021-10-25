''' Example plugin to extend functionality '''
from spydrnet.ir.cable import Cable as CableBase
from spydrnet.ir import Port, InnerPin, OuterPin


class Cable(CableBase):
    ''' This class extends the default Cable class '''


    def get_merge_port(self):
        print("Merging from physical")

    # def get_merge_port(self, port1, port2):
    #     print("Merging ports %s and %s" % (port1, port2))
