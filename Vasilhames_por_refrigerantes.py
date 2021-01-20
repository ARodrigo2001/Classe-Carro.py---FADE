vasilhames_brinde = 0
vasilhames_vizinhos = 2
vasilhames_vazios = 0
vasilhames_cheios = 0
consumo = 0
resultado = []


def brindes(vasilhames_cheios):
    global vasilhames_brinde, vasilhames_vizinhos, vasilhames_vazios, consumo, resultado
    
    if vasilhames_cheios >= 3:

        vasilhames_cheios = vasilhames_cheios - 3
        vasilhames_vazios = vasilhames_vazios + 3
        consumo = consumo + 3

        brindes(vasilhames_cheios)
        
    elif vasilhames_cheios == 2:
        vasilhames_cheios = vasilhames_cheios - 2
        vasilhames_vazios = vasilhames_vazios + 2
        consumo = consumo + 2
        
        brindes(vasilhames_cheios)
        
    elif vasilhames_cheios == 1:
        vasilhames_cheios = vasilhames_cheios - 1
        vasilhames_vazios = vasilhames_vazios + 1
        consumo = consumo + 1
        
        brindes(vasilhames_cheios)
    
    elif vasilhames_vazios >= 3:
        vasilhames_brinde = vasilhames_brinde + 1
        consumo = consumo + 1
        vasilhames_vazios = vasilhames_vazios - 2 
        
        brindes(vasilhames_cheios)
    
    elif vasilhames_vazios == 2:
        vasilhames_vizinhos = vasilhames_vizinhos - 1
        vasilhames_vazios = vasilhames_vazios + 1
        consumo = consumo + 1
        vasilhames_brinde = vasilhames_brinde + 1
        vasilhames_vazios = vasilhames_vazios - 2
        vasilhames_vizinhos = vasilhames_vizinhos + vasilhames_vazios
        vasilhames_vazios = vasilhames_vazios - vasilhames_vazios
        brindes(vasilhames_cheios)   
        
    elif vasilhames_vazios == 1 or vasilhames_vazios == 0:
        resultado.append(consumo)
        
    vasilhames_brinde = 0
    vasilhames_vizinhos = 2
    vasilhames_vazios = 0
    vasilhames_cheios = 0
    consumo = 0       

vasilhames_cheios = input()
run = vasilhames_cheios.split(' ')
for x in run:
    brindes(int(x))
    
print(*resultado)