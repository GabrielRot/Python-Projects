from random import shuffle
vAlun1 = str(input('Digite o Nome do Primeiro Aluno:'))
vAlun2 = str(input('Digite o Nome do Segundo Aluno:'))
vAlun3 = str(input('Digite o Nome do Terceiro Aluno:'))
vAlun4 = str(input('Digite o Nome do Quarto Aluno:'))
vLista = [vAlun1,vAlun2,vAlun3,vAlun4]
shuffle(vLista)
print ('A ordem será')
print (vLista)