# YouPy - YouTube Video Downloader
# Criado por puyune - 05/2025

import yt_dlp
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading
import os

def iniciar_download():
    progress['value'] = 0
    progresso_label.config(text="Progresso: 0%")
    link = link_var.get()
    if not link.startswith("https://www.youtube.com/"):
        messagebox.showerror("Erro", "Por favor, insira um link válido do YouTube.")
        return
    opcoes = escolher_qualidade()
    pasta = escolher_pasta()
    thread = threading.Thread(target=baixar_video, args=(link, pasta, opcoes))
    thread.start()

def escolher_qualidade():
    qualidade = qualidade_var.get()
    if qualidade == "melhor":
        return {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4'
        }
    elif qualidade == "video":
        return {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4'
        }
    elif qualidade == "audio":
        return {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
    else:
        return {'format': 'best'}

def escolher_pasta():
    pasta = pasta_var.get()
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    return pasta

def hook_progresso(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)
        if total:
            porcentagem = int(downloaded * 100 / total)
            progresso_label.config(text=f"Progresso: {porcentagem}%")
            progress['value'] = porcentagem
            root.update_idletasks()

def baixar_video(link, pasta, opcoes):
    ydl_opts = {
        'outtmpl': os.path.join(pasta, '%(title)s.%(ext)s'),
        'progress_hooks': [hook_progresso],
        'ffmpeg_location': '/usr/bin/ffmpeg'
    }
    ydl_opts.update(opcoes)
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        messagebox.showinfo("Download Concluído", "O vídeo foi baixado com sucesso!") 
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao baixar o vídeo. Erro: {e}")

root = tk.Tk()
root.title("YouPy - YouTube Video Downloader")
root.geometry("500x400")

tk.Label(root, text="Cole o link do vídeo aqui:").pack(pady=5)
link_var = tk.StringVar()
tk.Entry(root, textvariable=link_var, width=50).pack(pady=5)

tk.Label(root, text="Escolha a qualidade do vídeo:").pack(pady=5)
qualidade_var = tk.StringVar(value="melhor")
tk.Radiobutton(root, text="Vídeo e áudio em melhor qualidade", variable=qualidade_var, value="melhor").pack(pady=5)
tk.Radiobutton(root, text="Somente vídeo", variable=qualidade_var, value="video").pack(pady=5)
tk.Radiobutton(root, text="Somente áudio (mp3)", variable=qualidade_var, value="audio").pack(pady=5)

tk.Label(root, text="Caminho da pasta para salvar o vídeo:").pack(pady=5)
pasta_var = tk.StringVar()
tk.Entry(root, textvariable=pasta_var, width=50).pack(pady=5)

tk.Button(root, text="Baixar", command=iniciar_download).pack(pady=20)

progress = ttk.Progressbar(root, length=300, mode='determinate', maximum=100)
progress.pack(pady=10)

progresso_label = tk.Label(root, text="Progresso: 0%")
progresso_label.pack(pady=5)

root.mainloop()

#puyune ʕ•́ᴥ•̀ʔっ♡
