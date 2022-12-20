# Leia o nome de uma cidade e diga se ela começa com o nome Santo
cidade = input('Digite o nome da sua cidade: ').strip()
cidade = cidade.split()
if cidade[0] == 'santo' or cidade[0] == 'Santo':
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')
