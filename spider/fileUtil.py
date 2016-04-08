#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a FileIO module '

__author__ = 'XSunny'

import os

#文件工具 - 包含写字节文件和字符文件，并且可以存取map对象

def saveByteFile(fileName, data):
	#print fileName
	f = None
	try:
		if not os.path.isfile(fileName):
			f = open(fileName, "wb")
			f.write(data)
			print fileName, ' saved'
	except IOError, e:
		print "FileIO ERROR!"
	finally:
		if f:
			f.close()

def saveTextFile(fileName, data):
	f = None
	try:
		if not os.path.isfile(fileName):
			f = open(fileName, "w")
			f.write(data)
	except IOError, e:
		print "FileIO ERROR!"
	finally:
		if f:
			f.close()

#save vol info
def saveDBFile(fileName, map):
	pass

#return map
def readDBFile(fileName):
	pass