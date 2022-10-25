"""
VALIDE UM  CPF

"""
#cpf = 123.456.789-01
cpf = input('Digite um cpf')
tamanho_cpf = 14
condicao = True

if len(cpf) != tamanho_cpf:
    condicao = False
elif (cpf[3] != '.') or (cpf[7] != '.') or (cpf[-3] != '-'):
    condicao = False
else:
        for i in range(tamanho_cpf):
         if( i != 3 ) and (i != 7) and (i != 11):
            c = cpf[i]
         if (not c .isdigit()):
            condicao = False

if (condicao):
    print('Formato de CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')












