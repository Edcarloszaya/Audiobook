import tkinter as tk
from tkinter import filedialog
from gtts import gTTS
import fitz


class AudioBook:

    def __init__(self) -> None:
        pass

    def selecionar_arquivo(self):

        janela = tk.Tk()
        janela.withdraw()

        caminho_do_arquivo = filedialog.askopenfilename(
            title="Selecione o arquivo PDF", filetypes=[("Arquivos PDF", "*.pdf")]
        )
        return caminho_do_arquivo

    def extrair_texto(self, caminho_do_PDF):
        documento = fitz.open(caminho_do_PDF)
        texto = ""

        for page_num in range(len(documento)):
            pagina = documento.load_page(page_num)
            texto += pagina.get_text()

        return texto

    def comverti_texto(self, texto):
        if texto:
            tts = gTTS(text=texto, lang="en", slow=False)
            tts.save("audiobook.mp3")
            print("Audiobook criado!")
        else:
            print("Audiobook nao foi criado!")
