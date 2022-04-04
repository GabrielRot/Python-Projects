#Desafio22

#nome maiúsculo
nomeMai = input('digite seu nome: ')
varNome = nomeMai.upper()
print('Olá',varNome,'é um Prazer te Conhecer ^^')

#nome minúsculo
nomeMin = input('digite seu nome: ')
varNome1 = nomeMin.lower()
print('Olá',varNome1,'é um Prazer te Conhecer ^^')

#contador de strings com if else
nomecon = input('digite seu nome: ')
separar = nomecon.split()
juntar  = ''.join(separar)
contar  = len(juntar)
print('Olá',nomecon,'é um Prazer te Conhecer')
print('Seu nome Possui',contar,'Caractéres')
if contar > 25:
    print('Seu nome é bem grande')
else:
    print('Seu nome é bem curto')

#contador do primeiro nome
nomePri = input('digite seu nome: ')
split = nomePri.split()
nome21341 = split[0]
conta = len(nome21341)
print('Olá',nomePri,'Prazer te Conhecer ^^')
print('Seu Primeiro Nome Possui',conta,'Caractéres')
if conta > 8:
    print('Seu nome é bem grande')
else:
    print('Seu nome é bem curto')

#Desafio 23

#leitor de casas decimais
numero = str(input('Digite um Numero de 0 a 9999: '))
#if numero != [3]:
    #print('Seu numero excedeu o limite.')
#else:
print('O Digitado Foi',numero,
      '\n unidades: ',numero[3],
      '\n dezena:   ',numero[2],
      '\n centena:  ',numero[1],
      '\n milhar:   ',numero[0])

#Desafio 24

#leitor de nome
Cidade = str(input('Digite o Nome da Cidade: ')).strip()
print(Cidade[:5].upper() == 'Santo')

#Desafio 25

#leitor de nome
name = str(input('Digite seu Nome Completo: ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in name.lower()))

#Desafio 26 Primeira e última ocorrência de uma string
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição{}'.format(frase.rfind('A')))

#Exercício 27 – Primeiro e último nome de uma pessoa
fname = str(input('Digite seu nome: ')).strip()
sepnome = fname.split()
print('O seu primeiro nome é {}'.format(sepnome[0]))
print('seu ultimo nome é {}'.format(sepnome[len(sepnome)-1]))

