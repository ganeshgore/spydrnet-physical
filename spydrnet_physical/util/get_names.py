import logging
from spydrnet import ir
from types import GeneratorType

logger = logging.getLogger("spydrnet_logs")


def get_names(objects):
    """
    Returns name name of the verilog object (if the it contains name property)

    args:
        object(list[Cable, Port, Definition, Instance]): pass list of objects
    returns:
        (list[str]) : list of
    """
    names = []
    if not isinstance(objects, (list, tuple, GeneratorType)):
        objects = tuple(
            [
                objects,
            ]
        )
    for each in objects:
        if isinstance(each, (ir.Cable, ir.Port, ir.Definition, ir.Instance)):
            names.append(each.name)
        else:
            logger.warning("Skipping unsupport object %s", type(each))
    return names


def get_attr(objects, attr):
    """
    Returns specific attribute from the properties of the object

    args:
        object(list[Cable, Port, Definition, Instance]): pass list of objects
    returns:
        (list[str]) : list of
    """
    return [getattr(each, attr, None) for each in objects]
