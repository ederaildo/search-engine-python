
# Busca simples em Python

## Sobre

Implementação de uma busca simples em Python, onde o intuito é fazer uma busca por termos em todos os arquivos que estão no diretório `/data`.


## Tecnologias utilizadas

* Python 2.7.12
* Sublime Text
* [unittest - Unit Testing Framework](https://docs.python.org/3/library/unittest.html)

## Pré Requisitos

Para execução será necessário:

* Python 2.7.* ou maior
* [unittest - Unit Testing Framework](https://docs.python.org/3/library/unittest.html)

## Execução

Executar o comando:

```
python search.py "<termo(s)>"
```
por exemplo:

```
python search.py "paul almond"
```
O resultado da busca será parecido como o abaixo:

```
$ python search.py "paul almond"
Foram encontradas 2 ocorrências pelo termo "paul almond" 
Os arquivos que possuem "paul almond" são:
data/7-up.txt
data/captive-hearts.txt
```




## Testes

Os testes foram construídos sob o framework UnitTest. Para executar os testes basta executar o comando:

```
python -m unittest -v -b test
```
O resultado dos testes serão parecidos como o abaixo:

```
$python -m unittest -v -b test

test_excesso_argumentos (test.TestSearch) ... ok
test_performance1 (test.TestSearch) ... ok
test_performance2 (test.TestSearch) ... ok
test_performance3 (test.TestSearch) ... ok
test_sem_argumento (test.TestSearch) ... ok
test_termo_composto (test.TestSearch) ... ok
test_termo_composto_case_insensitive (test.TestSearch) ... ok
test_termo_composto_inverso (test.TestSearch) ... ok
test_termo_composto_inverso_case_insensitive (test.TestSearch) ... ok
test_termo_composto_inverso_upper (test.TestSearch) ... ok
test_termo_composto_upper (test.TestSearch) ... ok
test_termo_simples (test.TestSearch) ... ok
test_termo_simples_case_insensitive (test.TestSearch) ... ok
test_termo_simples_upper (test.TestSearch) ... ok

----------------------------------------------------------------------
Ran 14 tests in 7.781s

OK
```

## Contributors

**Ederaildo Fontes**

* [github/ederaildo](https://github.com/ederaildo)
* [linkedin/ederaildo](https://www.linkedin.com/in/ederaildo/)

## Licença