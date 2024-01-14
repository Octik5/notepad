from tkinter import *

def on_button_click():
    text_widget.delete("1.0", END)

def copy_text(event=None):
    text_widget.clipboard_clear()
    text_widget.clipboard_append(text_widget.selection_get())

def cut_text(event=None):
    copy_text()
    text_widget.delete("sel.first", "sel.last")

def paste_text(event=None):
    text_widget.insert(INSERT, text_widget.clipboard_get())

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

window = Tk()

# Цвет фона 121212
background_color = "#121212"

# Шрифт Rubik
font_style = ("Rubik", 16, "bold")

# Создаем кастомный стиль для кнопок
style = {"bg": background_color, "font": font_style, "relief": FLAT, "activebackground": "#888"}

# Многострочное поле для ввода текста
text_widget = Text(window, wrap="word", width=115, height=43, bg=background_color, fg="white", insertbackground="white")
text_widget.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Загружаем изображение для кнопки
image_path = 'C:\\Users\\Никитик\\PycharmProjects\\telegrambot\\icons\\outline_delete_white_24dp.png'
image = PhotoImage(file=image_path)

# Создаем кнопку с кастомным стилем
button = Button(window, image=image, width=80, height=80, command=on_button_click, **style)
button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Устанавливаем цвет фона окна
window.configure(bg=background_color)

# Устанавливаем шрифт для всего текста в виджете
text_widget.tag_configure("rubik", font=font_style)
text_widget.configure(font=font_style)

# Настройка распределения пространства
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=0)  # Фиксированный размер для кнопки
window.grid_columnconfigure(0, weight=1)

# Привязываем функции к событиям
button.bind("<Enter>", lambda event: button.config(bg="#888"))
button.bind("<Leave>", lambda event: button.config(bg=style["bg"]))
button.bind("<Button-1>", lambda event: button.config(bg="#666"))

# Добавляем контекстное меню
context_menu = Menu(window, tearoff=0)
context_menu.add_command(label="Копировать", command=copy_text)
context_menu.add_command(label="Вставить", command=paste_text)
context_menu.add_command(label="Вырезать", command=cut_text)

# Привязываем контекстное меню к текстовому виджету
text_widget.bind("<Button-3>", show_context_menu)

# Привязываем комбинации клавиш
text_widget.bind("<Control-c>", copy_text)
text_widget.bind("<Control-v>", paste_text)
text_widget.bind("<Control-x>", cut_text)

# Включаем возможность копирования и вставки
text_widget.config(state="normal")

window.title("Notepad")
window.geometry("932x758")
window.iconbitmap('C:\\Users\\Никитик\\PycharmProjects\\telegrambot\\icons\\logo.ico')

window.mainloop()