from __future__ import with_statement
from sikuli.Sikuli import *


assert(capture(0, 0, 100, 100) != None)
assert(capture(Region(0,0,100,100)) != None)
popup("please select a region")
assert(capture() != None)