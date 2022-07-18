'''

Library of Python projects by David Kundih.

'''

# ignore __pycache__ from forming inside the library directory.
import sys
sys.dont_write_bytecode = True

# meta data imports from the vandal library.
from kundih.misc._meta import (
    __author__,
    __copyright__,
    __credits__,
    __license__,
    __version__,
    __documentation__,
    __contact__,
    __donate__,
    __APPversion__,
)

# all contents.
from logistics import *
from vandal import *
from duality import *

from kundih.objects.kmeans import KSrednjeVrijednosti
from kundih.objects.dijkstra import Dijkstra
from kundih.objects.linreg import LinearnaRegresija
from kundih.objects.montecarlo import MonteCarlo