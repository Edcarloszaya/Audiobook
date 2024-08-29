import tkinter as tk
from tkinter import filedialog

class AudioBook():

    def __init__(self) -> None:
        pass

    def selecionar_arquivo(self):

        janela = tk.Tk()
        janela.withdraw()

        caminho_do_arquivo = filedialog.askopenfilename(title="Selecione o arquivo PDF",
                                                        filetypes=[("Arquivos PDF","*.pdf")])
        return caminho_do_arquivo
    
    

    
