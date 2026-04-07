#código Puro sem a Biblioteca do streamlits para rodar no front, somente via Console. Todo este código serviu como base para que o arquivo app.py pudesse ser feito com a biblioteca Streamlits.
numeros = []
especiais = []
maiu = []
minu = []
print('-----Bem vindo ao verificador de senha!-----')
print('--Insira a sua senha para que sela seja avaliada!--')
senha = input('Digite a sua senha informando todos os caracteres que ela contém: ')
quantidade = len(senha)
for char in senha:
    if char.isupper():
        maiu.append(char)
    elif char.islower():
        minu.append(char)
    elif char.isnumeric():
        numeros.append(char)
    else:
        especiais.append(char)

comprimento = min(quantidade * 5, 40)
num = min(len(numeros) * 15, 15)
simbolos = min(len(especiais) * 25, 25)
if maiu and minu:
    diversidade = 20
else:
    diversidade = 0
nota = comprimento + diversidade + num + simbolos

if comprimento > 0 and diversidade > 0 and num > 0 and simbolos > 0:
    status = 'Status: SENHA APROVADA'
else:
    status = 'Status: SENHA REPROVADA'

if 0 <= quantidade <= 4:
    print(f'Sua senha é muito fraca! \n Pontuação de senha>({nota} \n {status}')
elif 5 <= quantidade <= 7:
    if maiu and minu and numeros and especiais:
        print(f'Sua senha tem variedade mas é curta \n Pontuação de senha>({nota} \n {status} ')
    else:
        print(f'Sua senha é fraca \n Pontuação de senha>({nota} \n {status}' )
elif 8 <= quantidade <= 9:
    if maiu and minu and numeros and especiais:
        print(f'Sua senha é boa, mas pode ter mais caracteres para ficar melhor \n Pontuação de senha>({nota} \n {status}')
    else:
        print(f'Sua senha é boa, mas tem que melhorar a varidedade \n Pontuação de senha>({nota} \n {status}')
elif quantidade >= 10:
    if maiu and minu and numeros and especiais:
        print(f'Sua senha é segura \n Pontuação de senha>({nota} \n {status}')
    elif maiu and minu and numeros:
        print(f'Sua senha é grande, mas pode ter caracteres especiais para melhorar ainda mais \n Pontuação de senha>({nota} \n {status}')
    else:
        print(f'Sua senha é longa, mas não é forte, falta caracteres especiais, números e diferença entre letras maiúsculas e minúsculas. \n Pontuação de senha>({nota} \n {status}')