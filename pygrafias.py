from PyPDF2 import PdfReader
import os
import glob
import shutil
import tkinter as tk
from tkinter import filedialog

class DirectorySelectorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("pygrafias")

        self.master.geometry("300x200")

        window_width = self.master.winfo_width()
        window_height = self.master.winfo_height()

        space = (window_height*20)/4

        top_space = tk.Frame(master, height=space, width=window_width)
        top_space.pack(pady=(0, space))

        self.button1 = tk.Button(self.master, text="Selecione a pasta origem.", command=self.fonte_direc)
        self.button1.pack(pady=space)

        self.button2 = tk.Button(self.master, text="Selecionar a pasta destino.", command=self.destino_direc)
        self.button2.pack(pady=space)

        self.button3 = tk.Button(self.master, text="Selecionar o PDF.", command=self.pdf_direc)
        self.button3.pack(pady=space)

        self.space_label = tk.Label(self.master, text="")
        self.space_label.pack(pady=space)

        self.button4 = tk.Button(self.master, text="TRASNFERIR FOTOS!", command=self.transfer)
        self.button4.pack(pady=space)

    def fonte_direc(self):
        self.fonte = filedialog.askdirectory()

    def destino_direc(self):
        self.destino = filedialog.askdirectory()
    
    def pdf_direc(self):
        self.pdf_file = filedialog.askopenfilename()

    def transfer(self):
        pdf = PdfReader(self.pdf_file)

        archives = []

        for i in range(1, len(pdf.pages)):
            page = pdf.pages[i]
            page_text = page.extract_text()
            text_list = page_text.split('\n')
            updated_text_list = [text for text in text_list if text != ' ']
            for text in updated_text_list:
                archives.append(text.split('.')[0])


        del archives[0]
        cont = 1

        for file in glob.iglob(self.fonte+'/*'):
            archive = os.path.basename(file)

            if archive.split('.')[0] in archives:
                shutil.move(file, 'selecionadas/' + archive)
                print(f"{cont}. '{archive}' transferido com sucesso!")
            else:
                print(f"{cont}. '{archive}' não foi encontrado em {self.fonte}.")
            
            cont = cont + 1

def main():
    root = tk.Tk()
    app = DirectorySelectorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    