#ClassMapGenerator.py
#Opens ARMObject.h, finds all the classes, and adds an entry into the ARMCastLookupTable for each one.
#
#Composed by Samson
#
#6/29/2014
from __future__ import print_function
import os,sys

roseinclude = os.environ.get('ROSE_INCLUDE')
if type(roseinclude) == 'None' :
  print("ROSE_INCLUDE not found.")
  sys.exit(1)
roseinclude+="\\stpcad_arm\\ARMObject.h"  #we need the file ARMObject.h
file = open(roseinclude)
if file.closed:
  print("Error opening ARMObject.h")
  sys.exit(1)
outfile = open("classmappy.h",'w')
if outfile.closed:
  print("Error opening classmappy.h")
  sys.exit(1)

header = open("classhead")
if header.closed:
  print("Error opening top of header definining file \'classhead\'")
  sys.exit(1)

outfile.write("//Generated by ClassMapGenerator.py\n")
for line in header:
	if not(line[0:2]=='##'):	#Allow for comments in header with leading ## 
		outfile.write(line)
for line in file:
  if ('class ' in line) and not(('ARMObject' in line) or ('ARMCursor' in line)): #We want to make all the things that have an ARMCastTo... function
    classname = line[6:len(line)-2]
    outline = '\t{"' + classname.upper() + '",' + '&ARMCastTo' + classname + '},\n'
    outfile.write(outline)
outfile.write('};')