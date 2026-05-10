from random import randint
from time import sleep

computador = randint(1, 10) #Aqui é gerado um número aleatório entre 0 e 10
print('Olá, sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

acertou = False #Essa parte é pra armezar o resultado caso ele seja falso

palpites = 0 #Aqui é o contador

while not acertou:
    palpites += 1
    jogador = int(input('Qual o seu palpite: '))
    if computador == jogador:
         acertou = True #Condição pra saber se a resposta é igual a do computador
    else: 
         if jogador < computador: #Esta condição vai dizer se o número está mais a frente ou menos.
              print('Mais... Tente mais uma vez!')
         if jogador > computador:
              print('Menos... Tente mais uma vez!') 
print('Você acertou o palpite é {}, você acertou com {} tentativas.'.format(computador, palpites))
        
    
    
#Jeito que eu fiz

num1 = randint(1, 10)

print('-=-' * 20 )
print('BEM VINDO AO JOGO DE ADIVINHAÇÃO!')
print('-=-' * 20)


print('PROCESSANDO...')
sleep(2)

cont = 0

resp = int(input('Digite o número de 0 à 10, que você acha que é o certo: '))

while num1 != resp:
    cont += 1
    resp = int(input(('Você errou, tente novamente: ')))
if num1 == resp:
        print('Você acertou o número é {}, parabéns, você tentou {}x até acertar!'.format(num1, cont))


