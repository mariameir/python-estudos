# Primeiros exemplos
print('primeiro programa')

'''
python se importa com Indentação
exemplo:
print (1+
2)  --------- esse codigo se fosse rodado geraria um erro
'''

# Tipos Básicos
print(True)  # bollean
print(False)   # bollean
print(1+4)  # int
print("TEXTO")  # text
print('voce é ' + 3 * ' muito' + ' legal')  #iteração
# print (3+ '3') --- ambiguidade
print([1, 2, 3, 4])  # list
print({'nome': 'maria ' 'luis ', 'idade': '25 ' '25'})  # dict


idade = 25
if type(idade) is int:
    print('ok')
