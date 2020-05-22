#!/usr/bin/python3

import shutil
import sys

if len(sys.argv) > 2:
    (source, target) = sys.argv[1:]
else:
    (source, target)  = ('input.txt', 'output.txt')

try:
    shutil.copyfile(source, target)
except IOError as e:
    print("Unable to copy file. %s" % e)
except:
    print("Unexpected error:", sys.exc_info())