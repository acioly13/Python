from tkinter import *

# Cria a janena principal
window = Tk()

# Sea o titulo da janela
window.title("Hello World")

# Entrada de texto
text = Entry(window, width=50)
text.pack()
text.focus_set()


# Botão
def click_button():
    print(text.get())


bnt = Button(window, text="Click Me", width=20, command=click_button)
bnt.pack()
window.geometry("500x500")
window.mainloop()
