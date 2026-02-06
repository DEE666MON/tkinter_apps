import tkinter as tk

root = tk.Tk()
root.title("Ввод и вывод")
window_w, window_h = 800, 400
screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (screen_w - window_w) // 2, (screen_h - window_h) // 2
root.geometry(f"{window_w}x{window_h}+{x}+{y}")
root.resizable(False, False)
title = tk.Label(root, text="Введите имя и/или фамилию", font=("Arial", 18))
title.pack(pady=20)
entry_name = tk.Entry(root, font=("Arial", 18))
entry_name.pack(pady=5, ipady=4)
entry_lastName = tk.Entry(root, font=("Arial", 18))
entry_lastName.pack(pady=5, ipady=4)
message = tk.StringVar(value="")

def say_hello(event=None):
    name = entry_name.get().strip()
    lastName = entry_lastName.get().strip()
    if not name and not lastName:
        # result.config(text="Введите имя и/или фамилию :)")
        message.set("Введите имя и/или фамилию :)")
        entry_name.focus_set()
        return
    if any(symb.isdigit() for symb in name) or any(symb.isdigit() for symb in lastName):
        # result.config(text="Имя и/или фамилия не могут содержать цифры.")
        message.set("Имя и/или фамилия не могут содержать цифры.")
        return
    if name == "admin" or lastName == "admin":
        # result.config(text=f"Здравствуй, администратор.")
        message.set("Здравствуй, администратор.")
    elif name and lastName:
        # result.config(text=f"Здравствуй, {lastName} {name}.")
        message.set(f"Здравствуй, {lastName} {name}.")
    elif lastName:
        # result.config(text=f"Здравствуй, {lastName}.")
        message.set(f"Здравствуй, {lastName}.")
    else:
        # result.config(text=f"Здравствуйте, {name}.")
        message.set(f"Здравствуйте, {name}.")


btn = tk.Button(root, text="Поздоровоться",font=("Arial", 18), command=say_hello)
btn.pack(pady=10)


def clear(event=None):
    # result.config(text="")
    message.set("")
    entry_name.delete(0, tk.END)
    entry_lastName.delete(0, tk.END)
    entry_name.focus_set()
def on_close(event=None):
    root.destroy()

btn_clear = tk.Button(root, text="Очистить", font=("Arial", 18), command=clear)
btn_clear.pack(pady=10)

# result = tk.Label(root, text="", font=("Arial", 18))
result = tk.Label(root, textvariable=message, font=("Arial", 18))
result.pack(pady=(10, 0))

entry_name.focus_set()
root.bind("<Return>", say_hello)
root.bind("<F1>", clear)
root.bind("<Escape>", on_close)
root.mainloop()
