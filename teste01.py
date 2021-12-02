# entrada de dados
nome = input("Digite seu nome")
idade = input('digite sua idade')
# saida de dados
print('hello, ' + nome )
print('Você tem ' + idade + ' anos' )
#conversão de tipo de dado
idade = int(idade)
# calculo do tempo faltate para a posentadoria
comp = 75 - idade
# print tempo faltante para a aposentadoria
print( 'faltam ' ,  str(comp) , ' anos para a aposentadoria compulsória')

if idade >= 18:
    print('você pode ser preso')
    print('você pode votar')
    print('vote com sabedoria')

elif idade >= 16:
    print('você pode votar')
    print('vote com sabedoria')
else:
    print('Vá curtitr sua infância')
    


    


