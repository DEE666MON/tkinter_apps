import tkinter as tk

root = tk.Tk() # создание главного окна приложения
root.title("Моё первое Tkinter приложение")
# root.geometry("800x600")
window_w = 800
window_h = 600
# root.geometry(f"{window_w}x{window_h}")
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = (screen_w - window_w) // 2
y = (screen_h - window_h) // 2
root.geometry(f"{window_w}x{window_h}+{x}+{y}")
root.resizable(False, False)

def on_close(event=None):
    root.destroy()

label = tk.Label(root, text="Привет, это моё первое окно на Tkinter.", font=("Arial", 18))
label.pack(pady=25)
btn_close = tk.Button(root, text="Закрыть", command=on_close)
btn_close.pack(pady=30)
root.bind("<Escape>", on_close)
root.mainloop() # запускает цикл событий: клики, ввод, перерисовка окна