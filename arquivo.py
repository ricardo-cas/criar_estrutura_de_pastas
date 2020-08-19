import os # biblioteca responsável por acessar arquivos
import shutil # biblioteca responsável para realizar a movimentação de arquivos/pastas

def boas_vindas():
    print('Hello World')

def cria_pasta():
    nome_pasta = input('Qual o nome da Pasta?: ')


    if not os.path.exists(nome_pasta):
            print()
            os.makedirs(nome_pasta)
            print(f'A pasta "{nome_pasta}" foi criada!')
    else:
            print(f'Pasta "{nome_pasta}" já foi criada')

def exibe_caminho_atual():
    print('# ainda vou criar um metodo que exibe o caminho atual da pasta')


if __name__ == "__main__":
    boas_vindas()
    print()
    exibe_caminho_atual()
    cria_pasta()