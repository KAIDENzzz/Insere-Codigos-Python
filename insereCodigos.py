import pyautogui
import time
import os

def colar_codigos():
    # Solicita ao usuário o nome do arquivo (sem extensão)
    nome_arquivo = input("Digite o nome do arquivo: ").strip()
    if not nome_arquivo.lower().endswith(".txt"):
        nome_arquivo += ".txt"
    
    # Define o caminho do arquivo na pasta Documentos/txt
    caminho_arquivo = os.path.join(os.path.expanduser("~/Documentos/txt"), nome_arquivo)
    
    if os.path.exists(caminho_arquivo):
        print("O processo começará em 5 segundos...")
        time.sleep(5)
        
        try:
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
                        # Aguarda x segundos antes de continuar
                        time.sleep(1.0)
                        
                print("Processo concluído!")
        except Exception as e:
            print(f"Erro inesperado: {e}")
    else:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado na pasta Documentos/txt.")

if __name__ == "__main__":
    colar_codigos()