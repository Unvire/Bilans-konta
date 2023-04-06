from tkinter import filedialog as fd
from tkinter.messagebox import showerror
import tkinter as tk
import os

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bilans konta')
        self.geometry('250x150')

        self.frame = tk.Frame()
        self.buttonOpenFile = tk.Button(self.frame, text='Otwórz plik', command=lambda: self.countMoney())
        self.labelResult = tk.Label(self.frame, text='0,00 PLN', pady=10, font='Helvetica 18 bold', fg='#8B8000')
        self.buttonResult = tk.Button(self.frame, text='O programie', command=lambda: self.openAboutWindow())
        self.blankLabel = tk.Label(self.frame, text='')

        self.buttonOpenFile.grid(row=1, column=1)
        self.labelResult.grid(row=2, column=1)
        self.blankLabel.grid(row=3, column=1)
        self.buttonResult.grid(row=4, column=1)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

    def countMoney(self):
        filename = fd.askopenfilenames(initialdir=os.getcwd(), filetypes=(('Text files', '.txt'),)) # open file window (filetypes must be a tuple of tuples)
        with open(filename[0]) as file:
            try:
                outText = [float(line[:-4].replace(',','.').replace(' ','')) for line in file.readlines() if 'PLN' in line]
                result = sum(outText)
                self.labelResult['text'] = f"{'%.2f' %result} PLN"
                if result > 0:
                    self.labelResult['fg'] = '#02CC20'
                elif result < 0:
                    self.labelResult['fg'] = '#FF0000'
            except (ValueError, TypeError):
                tk.messagebox.showerror('Błąd', 'Niepoprawne dane w pliku tekstowym')

    def openAboutWindow(self):
        # make new TopLevel widged
        aboutWindow = AboutWindow()

### TO DO: wybor tylko pliku tekstowego

class AboutWindow(tk.Tk):
    def __init__(self):
        self.top = tk.Toplevel() # create toplevel widget
        self.frame = tk.Frame(self.top) # create frame in that widget
        self.top.title('O programie')
        self.top.geometry('550x100')
        self.line1Label = tk.Label(self.frame, text='Program liczy balans konta. Skopiowaną historię transakcji należy wkleić')
        self.line2Label = tk.Label(self.frame, text='do pliku tekstowego. Konieczne jest zeby kwoty były osobnymi wierszami i miały walutę PLN.')
        self.closeButton = tk.Button(self.frame, text='Zamknij', command=lambda: self.top.destroy()) # close window
        self.blankLabel = tk.Label(self.frame, text='')

        self.line1Label.grid(row=1, column=1)
        self.line2Label.grid(row=2, column=1)
        self.blankLabel.grid(row=3, column=1)
        self.closeButton.grid(row=4, column=1)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

if __name__ == '__main__':
    app = App()
    app.mainloop()