from random import *
import re
from time import *
date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
print asctime(date1)
print re.escape('ht+p')
print map(re.escape, {'1':'2', '3':'4'})
print re.escape("abc+d")
print map(lambda x: x, {'a':'b','c':'d'})
m = {'a':'b','c':'d'}
print m
