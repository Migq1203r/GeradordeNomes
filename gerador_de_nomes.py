import csv
import random
import sys
import os
def geradordenome():
    escolha = input("Digite M para nomes masculino e F para Feminino e S para sair:\n")
    if escolha.lower() == 'm':
        quantidade = 5
        with open('nomes_masculinos.csv', newline='', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)  # pula o cabeçalho
            nomes = [linha[0] for linha in leitor]
        quantidade = min(quantidade, len(nomes))
        nome_aleatorio = random.sample(nomes, quantidade)
        print("Nomes sorteados:")
        for nome in nome_aleatorio:
            print("-", nome)
        input("Pressione ENTER para Gerar Outro Nome: ")
        if os.name == 'nt':
            os.system('cls')

        else:
            os.system('clear')
        geradordenome()

    elif escolha.lower() == 'f':
        quantidade = 5
        with open('nomes_femininos.csv', newline='', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)  # pula o cabeçalho
            nomes = [linha[0] for linha in leitor]
        quantidade = min(quantidade, len(nomes))
        nome_aleatorio = random.sample(nomes, quantidade)
        print("Nomes sorteados:")
        for nome in nome_aleatorio:
            print("-", nome)
        input("Pressione ENTER para Gerar Outro Nome: ")
        if os.name == 'nt':
            os.system('cls')

        else:
            os.system('clear')
        geradordenome()
    elif escolha.lower() == 's':
        print("Saindo...")
        sys.exit()
    else:
        print("Opção não encontrada!")
        geradordenome()

geradordenome()