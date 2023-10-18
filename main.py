from tkinter import NW, FLAT

import yt_dlp
import tkinter as tk
from PIL import Image, ImageTk

import os
from tkinter import filedialog



def download(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"Downloaded {url}")

def save_path():
    folder_selected = filedialog.askdirectory()
    if os.path.exists('specs.ydlbl'):
        with open('specs.ydlbl', 'r') as f:
            content = f.read()
        start = content.find('[OUTPUT]')
        end = content.find('[ENDOUTPUT]')
        if start != -1 and end != -1:
            content = content[:start+8] + folder_selected + content[end:]
        else:
            content += '\n[OUTPUT]' + folder_selected + '[ENDOUTPUT]'
    else:
        content = '[OUTPUT]' + folder_selected + '[ENDOUTPUT]'
    with open('specs.ydlbl', 'w') as f:
        f.write(content)
    print(f"Path saved: {folder_selected}")




def run_gui():
    root = tk.Tk()
    root.title("Visor")
    root.configure(border=0, highlightthickness=0)
    root.geometry("700x700")
    root.resizable(False, False)

    canvas = tk.Canvas(root, height=700, width=700)
    canvas.configure(border=0, highlightthickness=0)
    canvas.pack()

    img = Image.open("assets/images/bg.png")
    img = img.resize((700, 700))
    img = ImageTk.PhotoImage(img)
    canvas.create_image((0,0), image=img, anchor=tk.N+tk.W)

    canvas.create_text((350, 40), text="Youtube Downloader", font="Helvetica 20 bold", fill="#e0e0e0")

    url_input = tk.Entry(canvas, width=50, font=("Helvetica", 15))
    canvas.create_window((350, 100), window=url_input, height=50)

    download_button = tk.Button(root, text="Download", font=("Helvetica", 15), bg="#e0e0e0", command=lambda: download(url_input.get()))
    download_button.configure(width=10, relief=FLAT)
    canvas.create_window((610, 655), window=download_button, height=50)

    path_button = tk.Button(root, text="Select Path", font=("Helvetica", 15), bg="#e0e0e0", command=save_path)
    path_button.configure(width=10, relief=FLAT)
    canvas.create_window((450, 655), window=path_button, height=50)


    root.mainloop()




if __name__ == '__main__':
    run_gui()

