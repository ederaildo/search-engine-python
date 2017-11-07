#!/usr/bin/python3
#-*- coding:utf-8 -*-


#***************************************************
# Search Engine simples em Python
# Autor: Ederaildo Fontes
#***************************************************

import os
import string
from os import listdir
from os.path import basename
import sys

DATA_DIR = "data"

def buscaTermo(conteudo, termo):
	conteudo = conteudo.lower()
	termoSplit = termo.split( )

	encontrou = True

	for t in termoSplit:
		if conteudo.find(t.lower()) == -1:
			encontrou = False
	
	if encontrou:
		return True

	return False


def busca(termo):
	arquivos = listdir(DATA_DIR)
	arquivos.sort()
	count = 0
	arquivosEncontrados = []

	for arq in arquivos:
		conteudo = open(DATA_DIR + "/" + arq, "r").read()

		if buscaTermo(conteudo, termo):
			#print file
			count +=1
			arquivosEncontrados.append(arq)


	print 'Foram encontradas {0} ocorrências pelo termo "{1}" '.format(count, termo)
	print 'Os arquivos que possuem "{0}" são:'.format(termo)
	
	for arqF in arquivosEncontrados:
		print "data/{0}".format(arqF)




try:
	busca(sys.argv[1])
except Exception as e:
	print "Erro: ", e
	raise

