#! /usr/bin/python

from ete3 import Tree
t = Tree('test.nw')
t.set_outgroup(t & "X")
print t.write()
