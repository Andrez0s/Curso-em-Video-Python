# Jogo de Jokenpô
import random

jokenpo = ('pedra', 'papel', 'tesoura')
escolha_computador = random.choice(jokenpo)
escolha_usuário = input('Escolha pedra papel ou tesoura ')

# Possibilidades onde o usuário ganha

if escolha_computador == 'pedra' and escolha_usuário == 'papel':
    print(f'Você ganhou! minha escolha foi {escolha_computador}')
elif escolha_computador == 'papel' and escolha_usuário == 'tesoura':
    print(f'Você ganhou! minha escolha foi {escolha_computador}')
elif escolha_computador == 'tesoura' and escolha_usuário == 'pedra':
    print(f'Você ganhou! minha escolha foi {escolha_computador}')

# Possibilidades onde o computador ganha

elif escolha_usuário == 'pedra' and escolha_computador == 'papel':
    print(f'Eu ganhei! minha escolha foi {escolha_computador}')
elif escolha_usuário == 'tesoura' and escolha_computador == 'pedra':
    print(f'Eu ganhei! minha escolha foi {escolha_computador}')
elif escolha_usuário == 'papel' and escolha_computador == 'tesoura':
    print(f'Eu ganhei! minha escolha foi {escolha_computador}')
else:
    print('Empate! jogue novamente')
