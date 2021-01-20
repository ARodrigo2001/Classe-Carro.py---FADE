entrada = input()
entrada = entrada.split(' ')
saida = 0
resultado = 0
operacoes = 0
loop_on = 0
   
def somar_operacoes():
    global op_on
    global op
    op = []
    op_on = 1

for x, y in enumerate(entrada):
    if y == "LOOP":
        loop = int(entrada[x + 1])
        loop_on = 1
        
    elif y == "OP":
        soma = int(entrada[x + 1])
        if loop_on == 1:
            operacoes = operacoes + soma
        elif loop_on == 0:
            resultado = resultado + soma
            soma = 0
        
    elif y == "FIMLOOP":
        resultado = resultado + (operacoes*loop)
        operacoes = 0
        loop_on = 0
        soma = 0
        
print(saida+resultado)