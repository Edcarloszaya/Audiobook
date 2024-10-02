from manager import AudioBook
from logo import logo


# instacia classe
audio = AudioBook()

def menu():
    audio.limpar_tela()
    print(logo)
    print("\nBem vindo ao AudioBook\n")

def main():

    execucao = True

    while execucao:
        
    #   menu
        menu()
        escolha = input(f"Para seleciona PDF tecla : [1] ? \nPara sair tecla: [x] ?")

        if escolha == '1':
            # busca pdf
            menu()
            PDF = audio.selecionar_arquivo()

            # extrai texto 
            if PDF:
                menu()
                texto = audio.extrair_texto(PDF)
            
                # comverter pra audio
                audio.converter_texto(texto)

            criar_novamemte = input('\nDesejar criar outro Audiobook: s=[Sim] ou n=[Nao] ?')
            if criar_novamemte == 's':
                execucao = False
                main()
                        
            else:
                execucao = False
                audio.limpar_tela()


        elif escolha != '1':
            execucao = False
            audio.limpar_tela()

        
main()