#!/usr/bin/python3
#-*- coding:utf-8 -*-

#***************************************************
# Teste do Search Engine 
# Autor: Ederaildo Fontes
#***************************************************

import unittest
import time
import search

MAX_SEGUNDOS = 120

# Classe para execução dos testes
class TestSearch(unittest.TestCase):

	# function test_performance1
	# executa o teste de performance onde o tempo de execução
	# não pode ser maior que o valor da constante MAX_SEGUNDOS
	def test_performance1(self):
		start = time.time()
		search.validarTermos(["search.py","john"])
		search.busca("john")
		segundos = time.time() - start
		self.assertLess(segundos, MAX_SEGUNDOS)

	# function test_performance2
	# executa o teste de performance onde o tempo de execução
	# não pode ser maior que o valor da constante MAX_SEGUNDOS
	def test_performance2(self):
		start = time.time()
		search.validarTermos(["search.py","michael"])
		search.busca("michael")
		segundos = time.time() - start
		self.assertLess(segundos, MAX_SEGUNDOS)

	# function test_performance2
	# executa o teste de performance onde o tempo de execução
	# não pode ser maior que o valor da constante MAX_SEGUNDOS
	def test_performance3(self):
		start = time.time()
		search.validarTermos(["search.py","disney"])
		search.busca("disney")
		segundos = time.time() - start
		self.assertLess(segundos, MAX_SEGUNDOS)

	#test_termo_simples dwayne
	# function test_termo_simples
	# executa um teste de busca com um termo simples
	# como o resultado é conhecido o valor deve ser maior que zero
	def test_termo_simples(self):
		retornoBusca = []
		search.validarTermos(["search.py","dwayne"])
		retornoBusca = search.busca("dwayne")
		self.assertGreater(retornoBusca[0], 0)

	# function test_termo_simples_upper
	# executa um teste de busca com um termo uppercase
	# o resultado deve ser igual ao mesmo termo lowercase
	def test_termo_simples_upper(self):
		retornoBusca = []
		retornoBuscaUpper = []
		retornoBusca = search.busca("dwayne")
		retornoBuscaUpper = search.busca("DWAYNE")
		self.assertEquals(retornoBusca[0], retornoBuscaUpper[0])

	# function test_termo_simples_case_insensitive
	# executa um teste de busca com um termo case insensitive
	# o resultado deve ser igual ao mesmo termo lowercase
	def test_termo_simples_case_insensitive(self):
		retornoBusca = []
		retornoBuscaCI = []
		retornoBusca = search.busca("dwayne")
		retornoBuscaCI = search.busca("DwaYne")
		self.assertEquals(retornoBusca[0], retornoBuscaCI[0])

	# function test_termo_composto
	# executa um teste de busca com um termo composto
	# como o resultado é conhecido o valor deve ser maior que zero
	def test_termo_composto(self):
		retornoBusca = []
		search.validarTermos(["search.py","john cusack"])
		retornoBusca = search.busca("john cusack")
		self.assertGreater(retornoBusca[0], 0)

	# function test_termo_composto_upper
	# executa um teste de busca com um termo composto uppercase
	# o resultado deve ser igual ao mesmo termo composto lowercase
	def test_termo_composto_upper(self):
		retornoBusca = []
		retornoBuscaUpper = []
		retornoBusca = search.busca("john cusack")
		retornoBuscaUpper = search.busca("JOHN CUSACK")
		self.assertEquals(retornoBusca[0], retornoBuscaUpper[0])

	# function test_termo_composto_case_insensitive
	# executa um teste de busca com um termo composto case insensitive
	# o resultado deve ser igual ao mesmo termo composto lowercase
	def test_termo_composto_case_insensitive(self):
		retornoBusca = []
		retornoBuscaCI = []
		retornoBusca = search.busca("john cusack")
		retornoBuscaCI = search.busca("JoHn CUsACK")
		self.assertEquals(retornoBusca[0], retornoBuscaCI[0])

	# function test_termo_composto_inverso
	# executa um teste de busca com um termo composto com palavras inversas
	# o resultado deve ser igual ao mesmo termo composto lowercase
	def test_termo_composto_inverso(self):
		retornoBusca = []
		retornoBuscaInverso = []
		retornoBusca = search.busca("john cusack")
		retornoBuscaInverso = search.busca("cusack john")
		self.assertEquals(retornoBusca[0], retornoBuscaInverso[0])

	# function test_termo_composto_inverso_upper
	# executa um teste de busca com um termo composto com palavras inversas em uppercase
	# o resultado deve ser igual ao mesmo termo composto lowercase
	def test_termo_composto_inverso_upper(self):
		retornoBusca = []
		retornoBuscaInverso = []
		retornoBusca = search.busca("john cusack")
		retornoBuscaInverso = search.busca("CUSACK JOHN")
		self.assertEquals(retornoBusca[0], retornoBuscaInverso[0])

	# function test_termo_composto_inverso_case_insensitive
	# executa um teste de busca com um termo composto com palavras inversas em case insensitive
	# o resultado deve ser igual ao mesmo termo composto lowercase
	def test_termo_composto_inverso_case_insensitive(self):
		retornoBusca = []
		retornoBuscaInverso = []
		retornoBusca = search.busca("john cusack")
		retornoBuscaInverso = search.busca("CusACK JohN")
		self.assertEquals(retornoBusca[0], retornoBuscaInverso[0])

	# function test_sem_argumento
	# executa um teste de busca sem passar argumentos
	# o resultado deve ser uma mensagem de exceção customizada
	def test_sem_argumento(self):
		with self.assertRaises(NameError) as ie:
			search.validarTermos(["search.py"])

		self.assertEqual(ie.exception.message, "Por favor digite o(s) termo(s) para busca.")

	# function test_excesso_argumentos
	# executa um teste de busca passando mais de 2 argumentos
	# o resultado deve ser uma mensagem de exceção customizada
	def test_excesso_argumentos(self):
		with self.assertRaises(NameError) as ie:
			search.validarTermos(["search.py","michael j fox", "john", "stephen hawking"])

		self.assertEqual(ie.exception.message, "Por favor digite corretamente o(s) termo(s) para busca.")


if __name__ == '__main__':
	unittest.main()
