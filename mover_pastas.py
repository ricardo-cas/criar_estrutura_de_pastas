import os # biblioteca responsável por acessar arquivos e pastas do sistema
import shutil # biblioteca responsável para realizar a movimentação de arquivos/pastas
from pathlib import Path
import json # biblioteca usada para ler arquivo com os nomes dos diretorios que as pastas serão criadas

def testa_move_Pasta():
    nome_pasta = input('Qual o nome da Pasta você deseja mover?: ')

    if not os.path.exists(nome_pasta):
            print("--------------------------------")
            print(f'A Pasta "{nome_pasta}" não existe!')
            print("################################")
    else:
        # origem = os.listdir('.')
        # print(origem)
        for item in os.walk(nome_pasta):
            print(item)
            print(os.getcwd())
            # os.chdir('.') # muda o diretório para a pasta criada
        # os.chdir(origem) # muda o diretório para a pasta criada
        # print(os.chdir(origem)) # muda o diretório para a pasta criada

def move_Pasta():
    nome_pasta = input('Qual o nome da Pasta você deseja mover?: ')

    if not os.path.exists(nome_pasta):
            print("--------------------------------")
            print(f'A Pasta "{nome_pasta}" não existe!')
            print("################################")
    else:        
        print("--------------------------------")
        print(f'A Pasta "{nome_pasta}" foi movida!')
        print("################################")

def exibe_caminho_atual():
    print("O Caminho da pasta é: ")
    print(os.getcwd())
    


def inicia_programa():
    print("--------------------------------")
    testa_move_Pasta()
    print("--------------------------------")



if __name__ == "__main__":
    inicia_programa()
    