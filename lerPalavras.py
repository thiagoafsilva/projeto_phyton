""" Le um arquivo texto e mostra o conteudo na tela. """

print __doc__
f = open('palavras_lingua_portuguesa.csv')
for linha in f:
	print linha.rstrip()
	int quantidade = linha.count('a')
	f.close()

	print '--- fim'

