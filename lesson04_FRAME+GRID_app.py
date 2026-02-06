import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tkinter FRAME+GRID")
window_w, window_h = 800, 400
screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (screen_w - window_w) // 2, (screen_h - window_h) // 2
root.geometry(f"{window_w}x{window_h}+{x}+{y}")
root.resizable(False, False)
outer = tk.Frame(root, padx=16, pady=16)
outer.pack(fill="both", expand=True)
title = tk.Label(outer, text="Регистрация", font=("Arial", 24, "bold"))
title.pack(anchor="w", pady=(0,12))
form = tk.Frame(outer)
form.pack(fill="x")
lbl_name = tk.Label(form, text="Имя:", font=("Arial", 16))
ent_name = tk.Entry(form, font=("Arial", 16))
lbl_mail = tk.Label(form, text="Почта:", font=("Arial", 16))
ent_mail = tk.Entry(form, font=("Arial", 16))
lbl_pass = tk.Label(form, text="Пароль:", font=("Arial", 16))
ent_pass = tk.Entry(form, font=("Arial", 16))
lbl_anotherPass = tk.Label(form, text="Повторите пароль:", font=("Arial", 16))
ent_anotherPass = tk.Entry(form, font=("Arial", 16))
#anchor(Растянуть) w - влево e - вправо n - вверх s - вниз nsew - во все стороны
lbl_name.grid(row=0, column=0, sticky="w", padx=(0, 10), pady=6)
ent_name.grid(row=0, column=1, sticky="ew", pady=6)
lbl_mail.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=6)
ent_mail.grid(row=1, column=1, sticky="ew", pady=6)
lbl_pass.grid(row=2, column=0, sticky="w", padx=(0, 10), pady=6)
ent_pass.grid(row=2, column=1, sticky="ew", pady=6)
lbl_anotherPass.grid(row=3, column=0, sticky="w", padx=(0, 10), pady=6)
ent_anotherPass.grid(row=3, column=1, sticky="ew", pady=6)
form.grid_columnconfigure(1, weight=2)
btns = tk.Frame(outer)
btns.pack(fill="x", pady=(16, 0))

def clear():
    ent_name.delete(0, tk.END)
    ent_mail.delete(0, tk.END)
    ent_pass.delete(0, tk.END)
    ent_anotherPass.delete(0, tk.END)
    ent_name.focus_set()
def submit(event=None):
    name = ent_name.get().strip()
    mail = ent_mail.get().strip()
    password = ent_pass.get().strip()
    anotherPassword = ent_anotherPass.get().strip()
    if not name or not mail or not password:
        messagebox.showwarning("Ошибка", "Заполните все поля!")
    else:
        if password == anotherPassword:
            messagebox.showinfo("Готово", f"Пользователь создан:\n{name};\n{mail}.")
            clear()
        else:
            messagebox.showwarning("Ошибка", "Пароли не совпадают.")

btn_submit = tk.Button(btns, text="Создать", command=submit)
btn_clear = tk.Button(btns, text="Очистить", command=clear)
btn_clear.pack(side="right", pady=5)
btn_submit.pack(side="right", pady=5)
ent_name.focus_set()
root.bind("<Return>", submit)
root.mainloop()