""" Exercício - sistema de perguntas e respostas """
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2? ',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5? ',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2? ',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
quantd_perguntas = sum(1 for pergunta in perguntas if 'Pergunta' in pergunta)

respostas_enviadas = []
respostas_totais = {
    'respostas_certas': [],
    'respostas_erradas': []
}
for _ in range(len(perguntas)):
    print(f"Opções: ")
    for opções in perguntas[_]['Opções']:
        print(opções)
    pergunta_resposta = input(perguntas[_]['Pergunta'])
    if pergunta_resposta == perguntas[_]['Resposta']:
        print("Acertou👍")
    else:
        print("Errou ❌")
     
    respostas_enviadas.append(pergunta_resposta)
    
for i, resposta in enumerate(respostas_enviadas):
    if resposta in perguntas[i]['Resposta']:
        respostas_totais['respostas_certas'].append(resposta)
    else:
        respostas_totais['respostas_erradas'].append(resposta)

print(f'De {quantd_perguntas} perguntas, acertou {len(respostas_totais["respostas_certas"])}')