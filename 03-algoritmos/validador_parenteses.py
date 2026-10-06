pilha = [] #Criamos uma pilha vazia para adicionarmos os parênteses ao longo da execução.
expressão = str(input('\nDigite a expressão: '))#Lê a expressão a ser adicionada.

for simbolo in expressão: #Laço de repetição para verificar cada '(' ')' 
                          #digitados na expressão, ou seja, vai percorrer todos os caraacteres.

    if simbolo == '(': #Se o caractere digitado for igual ao caractere '(', então adicione o caractere a pilha[]
            pilha.append(simbolo)
    elif simbolo == ')':#Senão se, a quantidade 'len(pilha)' dos números da pilha forem maior que 0,
                        #então remova o último elemento da pilha usando o 'pop'.

        if len(pilha) > 0: #AQUI É VERIFICADO SE A LISTA É VAZIA ANTES DE REMOVER O ELEMENTO.
            pilha.pop()

        else: #Senão adicionamos o caractere ')' a pilha. E depois acaba o código!
            pilha.append(')')
            break #Finalização do código.

print('-=' * 10)

if len(pilha) == 0: #Se a quantidade de caracteres ou expressões da pilha forem == 0, 0 é TRUE(VERDADEIRO), então a expressão está correta.
   print('A Expressão está válida!')
else:#Se a quantidade de caracteres ou expressão da pilha forem != 0, é FALSE(FALSO), então a expressão está errada.
    print('A Expressão está errada!\n')



        
