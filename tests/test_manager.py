import pytest
from unittest import mock
from audiobook.manager import AudioBook

@mock.patch('tkinter.filedialog.askopenfilename')
def test_selecionar_arquivo(mock_askopenfilename):
    # Configurando o mock para retornar um caminho de arquivo
    mock_askopenfilename.return_value = "/caminho/para/o/arquivo.pdf"

    audio = AudioBook()
    resultado = audio.selecionar_arquivo()

    assert resultado == "/caminho/para/o/arquivo.pdf"
    mock_askopenfilename.assert_called_once_with(
        title="Selecione o arquivo PDF", filetypes=[("Arquivos PDF", "*.pdf")]
    )

# Testando quando o usuário cancela
@mock.patch('tkinter.filedialog.askopenfilename')
def test_selecionar_arquivo_cancelar(mock_askopenfilename):
    # Configurando o mock para retornar None (indicando cancelamento)
    mock_askopenfilename.return_value = None

    audio = AudioBook()
    resultado = audio.selecionar_arquivo()

    assert resultado is None

def test_extrair_texto_pdf_valido(mocker):
    # Simula um PDF válido com uma página
    mock_document = mocker.MagicMock()
    mock_document.page_count = 1
    mock_page = mocker.MagicMock()
    mock_page.get_text.return_value = "Conteúdo da página"
    mock_document.load_page.return_value = mock_page

    with mock.patch('fitz.open', return_value=mock_document):
        classe = AudioBook()
        texto = classe.extrair_texto("caminho/para/pdf_valido.pdf")
        assert texto == "Conteúdo da página"


def test_converter_texto(mocker):
    with mock.patch('builtins.open') as mock_open:
        mock_open.return_value.__enter__.return_value.write.return_value = None

        classe = AudioBook()
        classe.converter_texto("Texto para converter")

        mock_open.assert_called_once_with("audiobook.mp3", "wb")
        
       

def test_barra_progresso_calculo():
    classe = AudioBook()

    classe.barra_progresso(50)
    saida = '[##########------------------] 50%'

    assert saida == '[##########------------------] 50%'