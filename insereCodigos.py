import pyautogui
import time
import os

def colar_codigos():
    # Solicita ao usuário o nome do arquivo (sem extensão)
    nome_arquivo = input("Digite o nome do arquivo: ").strip()
    if not nome_arquivo.lower().endswith(".txt"):
        nome_arquivo += ".txt"
    
    # Define o caminho para a pasta "documentos" no mesmo local do script
    pasta_documentos = os.path.join(os.path.dirname(os.path.abspath(__file__)), "documentos")
    caminho_arquivo = os.path.join(pasta_documentos, nome_arquivo)
    
    try:
        # Timer de 5 segundos antes de iniciar
        print("O processo começará em 5 segundos...")
        time.sleep(5)
        
        with open(caminho_arquivo, 'r') as arquivo:
            # Lê todas as linhas do arquivo
            codigos = arquivo.readlines()
            
            for codigo in codigos:
                codigo = codigo.strip()  # Remove quebras de linha ou espaços extras
                if codigo:
                    # Digita o código
                    pyautogui.write(codigo)
                    # Pressiona a tecla Enter
                    pyautogui.press('enter')
                    # Aguarda 0,5 segundos antes de continuar
                    time.sleep(0.5)
                    
            print("Processo concluído!")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado na pasta 'documentos'.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    colar_codigos()
