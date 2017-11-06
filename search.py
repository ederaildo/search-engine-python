
#***************************************************
# Search Engine simples em Python
# Autor: Ederaildo Fontes
#***************************************************

import os
import string
from os import listdir
from os.path import basename, isdir, isfile
import sys

DATA_DIR = "data"

def search(termo):
	files = listdir(DATA_DIR)

	#for f in files:
		#print f
	print termo[1]



try:
	search(sys.argv)
except Exception as e:
	print "Erro: ".format(e.errno,e.strerror)
	raise

