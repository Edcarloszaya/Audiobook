import tkinter as tk
from tkinter import filedialog
from gtts import gTTS
import fitz
import sys
import os



class AudioBook:

    def __init__(self) -> None:
        pass

    def selecionar_arquivo(self):
        print('\nSelecionar seu PDF!!!')
        janela = tk.Tk()
        janela.withdraw()

        caminho_do_arquivo = filedialog.askopenfilename(
            title="Selecione o arquivo PDF", filetypes=[("Arquivos PDF", "*.pdf")]
        )
        return caminho_do_arquivo

    def extrair_texto(self, caminho_do_PDF):
        print("\nextraindo texto !....")
        documento = fitz.open(caminho_do_PDF)
        texto = ""

        total_paginas = documento.page_count

        for i in range(total_paginas):
            pagina = documento.load_page(i)
            texto += pagina.get_text()
            perc = (i + 1) * 100 / total_paginas
            self.barra_progresso(perc)
            print("\nTexto extraído com sucesso!")

        return texto

    def converter_texto(self, texto):
        print(f"\nComvertendo seu pdf em audio!\nTempo estimado pelo tamanho do pdf!....\nPfv espere termina...!!!")
        if texto:
            tts = gTTS(text=texto, lang="en", slow=False)
            tts.save("audiobook.mp3")
            print("\nAudiobook criado!")
        else:
            print("Audiobook nao foi criado!")

    def barra_progresso(self,perc):
        largura = 50
        bloco = int(round(largura * perc / 100))
        progresso = "#" * bloco + "-" * (largura - bloco)
        sys.stdout.write(f"\r[{progresso}] {perc}%")
        sys.stdout.flush()

    def limpar_tela(self):
        # Verifica o sistema operacional
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix/Linux/MacOS
            os.system('clear')