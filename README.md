# YouPy - Instalador de Vídeos do YouTube

O **YouPy** é um script Python simples e eficiente que permite baixar vídeos do YouTube de forma prática e rápida. Ele oferece opções para escolher a qualidade do download e o local de armazenamento do arquivo.

## Índice

1. [Introdução](#1-introdução)
2. [Requisitos](#2-requisitos)
    - [Instalando o Python](#21-instalando-o-python)
    - [Instalando o yt-dlp](#22-instalando-o-yt-dlp)
3. [Funcionamento do Código](#3-funcionamento-do-código)
    - [Função escolher_qualidade()](#31-função-escolher_qualidade)
    - [Função escolher_pasta()](#32-função-escolher_pasta)
    - [Função baixar_video()](#33-função-baixar_video)
    - [Função main()](#34-função-main)
4. [Como Utilizar](#4-como-utilizar)
    - [Passo 1: Executar o Script](#41-passo-1-executar-o-script)
    - [Passo 2: Inserir o Link do Vídeo](#42-passo-2-inserir-o-link-do-vídeo)
    - [Passo 3: Escolher o Tipo de Download](#43-passo-3-escolher-o-tipo-de-download)
    - [Passo 4: Escolher a Pasta de Salvamento](#44-passo-4-escolher-a-pasta-de-salvamento)
    - [Passo 5: Aguardar o Download](#45-passo-5-aguardar-o-download)
5. [Exemplo de Execução](#5-exemplo-de-execução)
6. [Licenciamento e Uso](#6-licenciamento-e-uso)
7. [Considerações Finais](#7-considerações-finais)

---

## 1. Introdução

O **YouPy** é um script Python que permite baixar vídeos do YouTube de forma rápida e prática. Você pode escolher a qualidade do conteúdo e também selecionar a pasta de destino para o arquivo.

## 2. Requisitos

Antes de executar o **YouPy**, você precisa garantir que possui o Python e a biblioteca **yt-dlp** instalados no seu sistema.

### 2.1. Instalando o Python

O Python pode ser instalado a partir do [site oficial](https://www.python.org/downloads/) ou via gerenciadores de pacotes, dependendo do seu sistema operacional.

### 2.2. Instalando o yt-dlp

O **yt-dlp** é a biblioteca utilizada para fazer o download dos vídeos. Para instalá-la, basta rodar o seguinte comando no terminal:

```bash
pip install yt-dlp
3. Funcionamento do Código
O código é dividido em algumas funções principais. Cada uma delas realiza uma parte do processo de download de vídeos:

3.1. Função escolher_qualidade()
Esta função permite que o usuário escolha o tipo de download que deseja:

1: Baixar vídeo e áudio na melhor qualidade disponível.

2: Baixar apenas o vídeo.

3: Baixar apenas o áudio (formato MP3).

3.2. Função escolher_pasta()
A função solicita ao usuário o caminho da pasta onde o vídeo será salvo. Caso o usuário não forneça um caminho, o vídeo será salvo no diretório atual do script. Se a pasta não existir, ela será criada automaticamente.

3.3. Função baixar_video()
Essa função é responsável por realizar o download do vídeo, utilizando as opções selecionadas nas funções anteriores. O vídeo será salvo na pasta escolhida pelo usuário.

3.4. Função main()
A função principal do script. Ela inicia o processo, solicitando o link do vídeo, chamando as funções de escolha de qualidade e pasta, e executando o download.

4. Como Utilizar
4.1. Passo 1: Executar o Script
Execute o script no terminal ou em uma IDE Python. O comando para executar o script pode ser:

bash
Copiar
Editar
python3 /caminho/para/o/script/youpy.py
4.2. Passo 2: Inserir o Link do Vídeo
O script irá solicitar o link do vídeo que deseja baixar. Copie o link diretamente da página do YouTube e cole-o no prompt do terminal.

4.3. Passo 3: Escolher o Tipo de Download
Escolha a qualidade do vídeo e do áudio conforme a sua preferência. As opções são:

1: Vídeo e áudio em melhor qualidade.

2: Somente o vídeo.

3: Somente o áudio (MP3).

4.4. Passo 4: Escolher a Pasta de Salvamento
O script irá pedir o caminho da pasta onde o vídeo será salvo. Caso não forneça um caminho, o vídeo será salvo na pasta atual.

4.5. Passo 5: Aguardar o Download
O script começará a baixar o vídeo. Ao final do processo, será exibida uma mensagem indicando que o download foi concluído com sucesso.

5. Exemplo de Execução
Aqui está um exemplo de como a interação no terminal pode acontecer:

bash
Copiar
Editar
Bem-vindo ao YouPy, seu instalador de vídeos!
Cole o link do vídeo aqui: https://youtu.be/jnaAgLZIqT0
Escolha o tipo de download:
1. Vídeo e áudio em melhor qualidade
2. Somente vídeo
3. Somente áudio(mp3)
Digite sua escolha (1, 2 ou 3): 1
Digite o caminho da pasta onde deseja salvar o vídeo: /home/usuario/Downloads
Baixando para a pasta: /home/usuario/Downloads
Download concluído com sucesso!
6. Licenciamento e Uso
O código do YouPy é oferecido de forma gratuita para uso pessoal e educacional. Você pode distribuir livremente, desde que mantenha a integridade do código e não altere ou remova o aviso de licenciamento.

A venda ou comercialização direta do código ou de qualquer parte dele é estritamente proibida. O YouPy pode ser compartilhado gratuitamente, mas não pode ser revendido ou distribuído como parte de produtos pagos.

7. Considerações Finais
O YouPy é uma ferramenta simples e prática para quem deseja baixar vídeos do YouTube de forma rápida e flexível. Ele permite escolher a qualidade do conteúdo e o local de armazenamento. Se você tiver sugestões ou encontrar algum problema, sinta-se à vontade para modificar o código ou entrar em contato com o desenvolvedor.

Criado por Yune | License: MIT
ʕ•́ᴥ•̀ʔっ♡
