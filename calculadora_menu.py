from time import sleep
resposta = 0
num1 = int(input('Digite o primeiro número: ')) #Duas váriaveis que armazena resposta.
num2 = int(input('Digite o segundo número: '))
while resposta != 5:
       print('''
      [1] Somar
      [2] Multiplicar
      [3] Maior     
      [4] Novos Números
      [5] Sair do programa''') #Aqui é o menu de respostas
    
       resposta = int(input('>>>>> Qual é a sua opção: '))
    
       if resposta == 1:
            soma = print('A soma entre {} + {} é = {}'.format(num1, num2, num1 + num2)) #Aqui é feita a soma
       elif resposta == 2:
            multi = print('A multiplicação entre {} x {} = {}'.format(num1, num2, num1 * num2))#Aqui é feita a multiplicação
       elif resposta == 3:
            if num1 > num2:
             print('O maior número entre {} e {} é {}'.format(num1, num2, num1))
            else: #Aqui a gente testa a condição pra saber qual é o maior e o menor.
                 print('O maior número entre {} e {} é {}'.format(num1, num2, num2)) 
       elif resposta == 4: #Condição pra informar uma resposta novamente
            print('Informe os números novamente!')
            num1 = int(input('Primeiro Valor: '))   #Só fez atualizar as váriaveis num1 e num2
            num2 = int(input('Segundo Valor: ')) 
       elif resposta == 5:
            sleep(0.8) #Aqui é pra dar programa finalizado igual indica no menu, bem simples!
            print('Programa Finalizado!')

       else: #Esta parte é para qualquer resposta que seja diferente das citadas acima ela seja uma opção inválida!
            resposta = int(input(('Opção Inválida. Tente Novamente: ')))
       print('=-=' * 10)
            
             





