import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Мини-редактор текста")
window_w, window_h = 800, 600
screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (screen_w - window_w) // 2, (screen_h - window_h) // 2
root.geometry(f"{window_w}x{window_h}+{x}+{y}")
root.resizable(False, False)

area = tk.Frame(root)
area.pack(fill="both", expand=True)
scroll = tk.Scrollbar(area)
scroll.pack(side="right", fill="y")
text = tk.Text(area, yscrollcommand=scroll.set)
text.pack(side="left", fill="both", expand=True)
scroll.config(command=text.yview)
buttons = tk.Frame(root)
buttons.pack(fill="x")

def openFile():
    path = filedialog.askopenfilename(
        title="Открыть файл",
        filetypes=[("Текстовый файл", "*.txt"), ("Все файлы", "*.*")]
    )
    if not path:
        messagebox.showwarning("Внимание", "Отсутствует путь к файлу.")
        return
    print(path)
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        clearText()
        text.insert("1.0", content)
        root.title(f"Мини-редактор текста — {path}")
    except Exception as ex:
        messagebox.showerror("Ошибка", f"Не удалось открыть/прочиать файл.\n{ex}")
def saveFile():
    path = filedialog.asksaveasfilename(
        title="Сохранить файл",
        defaultextension=".txt",
        filetypes=[("Текстовый файл", "*.txt"), ("Все файлы", "*.*")]
    )
    if not path:
        messagebox.showwarning("Внимание", "Отсутствует путь к файлу.")
        return
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text.get("1.0", tk.END))
        root.title(f"Мини-редактор текста — {path}")
    except Exception as ex:
        messagebox.showerror("Ошибка", f"Не удалось сохранить файл.\n{ex}")
def clearText():
    text.delete(0, tk.END)

btnOpen = tk.Button(buttons, text="Открыть файл", command=openFile, font=("Arial",18))
btnOpen.pack(side="left", padx=5, pady=5)
btnOpen = tk.Button(buttons, text="Сохранить файл", command=saveFile, font=("Arial",18))
btnOpen.pack(side="left", padx=5, pady=5)
btnClear = tk.Button(buttons, text="Очистить", command=clearText, font=("Arial",18))
btnClear.pack(side="right", padx=5, pady=5)
root.mainloop()