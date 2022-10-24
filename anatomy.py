#!/usr/bin/python

# Exaple Python script

import sys

argc = len(sys.argv)

if argc > 1:
    print('Too many args')

else:

    where = 'world'
    print ("hello", where)

print ('Googbye from' + sys.argv[0])

