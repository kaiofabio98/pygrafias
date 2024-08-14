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

        self.button1 = tk.Button(self.master, text="Selecione a pasta origem", command=self.fonte_direc)
        self.button1.pack(pady=space)

        self.button2 = tk.Button(self.master, text="Selecionar a pasta destino", command=self.destino_direc)
        self.button2.pack(pady=space)

        self.button3 = tk.Button(self.master, text="Selecionar o PDF", command=self.pdf_direc)
        self.button3.pack(pady=space)

        self.space_label = tk.Label(self.master, text="")
        self.space_label.pack(pady=space)

        self.button4 = tk.Button(self.master, text="Transferir!", command=self.transfer)
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
        for file_full in  glob.iglob(self.fonte+'/*'):
            transf = False
            file = os.path.basename(file_full)
            for archive in archives:
                if archive.endswith(file.split('.')[0]):
                    shutil.move(file_full, os.path.join(self.destino, file))
                    print(f"{cont}. '{file}' transferido com sucesso!")
                    cont = cont+1
                    transf = True

                    break
            
            if transf:
                pass
            else:
                print(f"{cont}. '{file}' não está no PDF de fotos escolhidas.")
                cont = cont + 1

def main():
    root = tk.Tk()
    app = DirectorySelectorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    