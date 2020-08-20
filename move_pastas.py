import os # biblioteca responsável por acessar arquivos
import shutil # biblioteca responsável para realizar a movimentação de arquivos/pastas
from pathlib import Path
import json # biblioteca usada para ler arquivo com os nomes dos diretorios que as pastas serão criadas

def boas_vindas():
    print('Hello World')

def cria_pasta():
    nome_pasta = input('Qual o nome da Pasta?: ')

    if not os.path.exists(nome_pasta):
            print("--------------------------------")
            os.makedirs(nome_pasta)
            print(f'A pasta "{nome_pasta}" foi criada!')
            print("--------------------------------")
            os.chdir(nome_pasta) # muda o diretório para a pasta criada
    else:
            print("--------------------------------")
            print(f'Pasta "{nome_pasta}" já foi criada')
            print("--------------------------------")
    os.chdir('.')


def exibe_caminho_atual():
    print("O Caminho da pasta é: ")
    print(os.getcwd())


def inicia_programa():
    boas_vindas()
    print("--------------------------------")
    exibe_caminho_atual()
    print("--------------------------------")
    cria_pasta()
    print("--------------------------------")