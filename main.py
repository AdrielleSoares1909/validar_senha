""" 

     Validador de senha:

        Regras:

            mínimo 8 caracteres

            tem número

            tem letra maiúscula 

"""


senha = str(input("Digite sua senha: ")) # pedir a senha

tamanho = len(senha) # calcular o tamanho corretamente

existe_numero = False

letra_maiuscula = False

for caracter in senha:
    if caracter.isdigit():
        existe_numero = True
        
for caracter in senha:
    if caracter.isupper():
        letra_maiuscula = True


if tamanho >= 8 and existe_numero and letra_maiuscula:
    print("Senha Valida!")
else:
    print("Senha invalida!")


