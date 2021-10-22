''' Example plugin to extend functionality '''
from spydrnet.ir.cable import CableBase

class Cable(CableBase):
    ''' Extending definition class '''

    def get_merge_port(self):
        print("Merging from physical")

    # def get_merge_port(self, port1, port2):
    #     print("Merging ports %s and %s" % (port1, port2))
