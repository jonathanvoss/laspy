from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import sys

onpy3 = sys.version_info[0] >= 3


if onpy3:
    xrange = range
