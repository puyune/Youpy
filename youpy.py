# YouPy - YouTube Video Downloader
# Licença: Uso livre para fins pessoais e educacionais.
# Não é permitido vender ou distribuir para fins comerciais.
# Distribuição gratuita é permitida, mas a venda não é autorizada.
# Criado por puyune - 05/2025
import yt_dlp
import os

def escolher_qualidade():
    print("\nEscolha o tipo de download:")
    print("1. Vídeo e áudio em melhor qualidade")
    print("2. Somente vídeo")
    print("3. Somente áudio(mp3)")

    escolha = input ("Difite sua escolha (1, 2 ou 3): ")
    if escolha == "1":
        return {'format': 'best'}
    elif escolha == "2":
        return {'format': 'bestvideo'}
    elif escolha == "3":
        return {'format': 'bestaudio/best'}
    else:
        print("Opção inválida. Usando a melhor qualidade por padrão.")
        return {'format': 'best'}
    
def escolher_pasta():
    pasta = input("Digite o caminho da pasta onde deseja salvar o video:")

    if pasta == "":
        pasta = os.getcwd()

    if not os.path.exists(pasta):
        print("A pasta não existe. Criando a pasta...")
        os.makedirs(pasta)
    
    return pasta

def baixar_video(link, pasta, opcoes):
    print(f"\nBaixando para a pasta: {pasta}")

    ydl_opts = {
        'outtmppl': os.path.join(pasta, '%(title)s.%(ext)s')
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        print("\nDownload concluído com sucesso!")

def main():
    print("Bem vindo ao YouPy seu instalador de videos!\n")
    link = input("Cole o link do video aqui:")

    opcoes = escolher_qualidade()
    pasta = escolher_pasta()

    baixar_video(link, pasta, opcoes)
if __name__ == "__main__":
    main()

#puyune ʕ•́ᴥ•̀ʔっ♡