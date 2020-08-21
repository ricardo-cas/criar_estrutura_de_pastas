import os # biblioteca responsável por acessar arquivos e pastas do sistema
import shutil # biblioteca responsável para realizar a movimentação de arquivos/pastas
from pathlib import Path
import json # biblioteca usada para ler arquivo com os nomes dos diretorios que as pastas serão criadas


# método que cria arquivo baseado na entrada do usuario
def cria_arquivo():
    nome_arquivo = input('Qual o nome do arquivo que você deseja criar? ')

    if not os.path.exists(nome_arquivo):
        Path(nome_arquivo).touch()
    else:
        print(f'Arquivo "{nome_arquivo}" já existe.')


if __name__ == "__main__":
    cria_arquivo()