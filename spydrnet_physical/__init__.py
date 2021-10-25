# pylint: skip-file
# Release data
import os
import glob
from spydrnet.parsers import parse
from spydrnet_physical import release

__author__ = '%s <%s>' % (release.authors['gore'])
__license__ = release.license

__date__ = release.date
__version__ = release.version
__release__ = release.release

base_dir = os.path.dirname(os.path.abspath(__file__))
