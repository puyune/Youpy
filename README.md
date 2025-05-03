# YouPy - YouTube Video Downloader

**Licença:**  
- **Uso livre** para fins pessoais e educacionais.  
- **Proibido vender ou distribuir para fins comerciais.**  
- **Distribuição gratuita** é permitida, mas a venda não é autorizada.  
- Criado por **puyune** - 05/2025

---

## Descrição

O **YouPy** é um simples downloader de vídeos do YouTube, que permite fazer o download de vídeos em diferentes qualidades (vídeo + áudio, apenas vídeo ou apenas áudio). O programa utiliza a biblioteca `yt-dlp` e uma interface gráfica desenvolvida com `tkinter` para facilitar o uso.

---

## Funcionalidades

- **Baixar vídeos do YouTube**: Basta inserir o link do vídeo desejado.
- **Escolher a qualidade**: Você pode escolher entre:
  - Melhor qualidade de vídeo + áudio.
  - Somente vídeo.
  - Somente áudio (formato MP3).
- **Escolher o diretório de destino**: Você pode selecionar onde o vídeo será salvo.
- **Interface gráfica simples**: Desenvolvido com `tkinter` para uma experiência mais amigável.

---

## Requisitos

- **Python 3.x**: Este projeto foi desenvolvido e testado com Python 3.
- **Dependências**:
  - `yt-dlp`: Para realizar o download dos vídeos.
  - `tkinter`: Para a interface gráfica.
  - `ffmpeg`: Necessário para converter o áudio para o formato MP3.

Você pode instalar as dependências com o seguinte comando:

```bash
pip install yt-dlp
```

O **ffmpeg** pode ser instalado a partir do seu gerenciador de pacotes, como:

### No Ubuntu/Debian:

```bash
sudo apt install ffmpeg
```

---

## Como usar

1. **Baixar o código**: Clone o repositório ou baixe o código.
2. **Instalar dependências**: Certifique-se de ter as bibliotecas necessárias, como mencionado na seção "Requisitos".
3. **Executar o programa**:
   - Basta rodar o script `youpypy.py`.
   - Insira o link do vídeo do YouTube, escolha a qualidade desejada e selecione a pasta onde deseja salvar o arquivo.
   - Clique no botão "Baixar" para iniciar o download.

---

## Contribuição

Este projeto está aberto para contribuições! Se você encontrar algum bug ou desejar sugerir melhorias, fique à vontade para abrir uma **issue** ou **pull request**.

---

## Licença

Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
