# Robô Linear - QUESTÃO 1  e 2

# QUESTÃO 1 / RESPOSTA - 2 METROS
# QUESTÃO 2 / RESPOSTA - APENAS A LETRA D ( SEQUÊNCIA FTFFTTFF )

print('''
Insira os movimentos desejados de acordo com a legenda abaixo:

F - Frente
T - Trás
''')

lista1 = (input('Insira uma lista de movimentos(exemplo: tffttftftt):'))

u = list(lista1)
h = False
while h == False:
    
    if len(u) == 0:
        break
    
    else:
        for i in u: 
       
            if i == 't':
                for x in u:
                    if x == 'f':
                        u.remove('f')
                        u.remove('t')
                        i = 0
                        x = 0
                        break
                    elif 'f' not in u:
                        h = True
                        break
                    
            elif 't' not in u:
                h = True
                break
        
            elif 'f' not in u:
                h = True
                break
                
if 'f' in u:
    print('O robô está a %d metros de distância da sua posição inicial.' %len(u))
elif 't' in u:
    print('O robô está a %d metros de distância da sua posição inicial.' %len(u))
elif len(u) == 0:
    print('O robô está na sua posição inicial')
