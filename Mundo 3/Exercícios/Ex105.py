# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações: A > Quantidade de notas, B > A maior nota, C > Menor nota
# D > Média da turma, E > Situação opcional

def notas(*n, sit=False):
    r = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': sum(n) / len(n)}
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(5, 6, 7.8, 9, sit=True)
print(resp)
