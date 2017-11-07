#!/usr/bin/python3
#-*- coding:utf-8 -*-

#***************************************************
# Search Engine simples em Python
# Autor: Ederaildo Fontes
#***************************************************

import os
from os import listdir
import sys
import datetime, time

DATA_DIR = "data"

def validarTermos(argumentos):
	try:
		termos = argumentos[1].lower()
	except IndexError as e:
		raise NameError,  "Por favor digite o(s) termo(s) para busca."

	if len(argumentos) <> 2:
		raise NameError, "Por favor digite corretamente o(s) termo(s) para busca."

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
	retorno = []

	for arq in arquivos:
		conteudo = open(DATA_DIR + "/" + arq, "r").read()

		if buscaTermo(conteudo, termo):
			#print file
			count +=1
			arquivosEncontrados.append(arq)

	print 'Foram encontradas {0} ocorrências pelo termo "{1}" '.format(count, termo)
	print 'Os arquivos que possuem "{0}" são:'.format(termo)
	retorno.append(count)
	retorno.append(termo)
	
	for arqF in arquivosEncontrados:
		print "data/{0}".format(arqF)
	return retorno

def main():
    pass

if __name__ == "__main__":
	main()
	try:
		retornoBusca = []
		start = time.time()
		validarTermos(sys.argv)
		retornoBusca = busca(sys.argv[1])
		segundos = time.time() - start
	except Exception as e:
		print "Erro: ", e


