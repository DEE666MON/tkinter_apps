import tkinter as tk

root = tk.Tk()
root.title("Tkinter app1")
window_w, window_h = 800, 400
screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (screen_w - window_w) // 2, (screen_h - window_h) // 2
root.geometry(f"{window_w}x{window_h}+{x}+{y}")
root.resizable(False, False)

app = tk.Frame(root)
app.pack(fill="both", expand=True)
sidebar = tk.Frame(app, width=200)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)
content = tk.Frame(app)
content.pack(side="left", fill="both", expand=True)

tk.Label(sidebar, text="Меню", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(anchor="w", pady=(0, 12))
pages = {}
menu_buttons = {}
def create_page(name="", title_text=""):
    if name != "" and title_text != "":
        page = tk.Frame(content)
        label = tk.Label(page, text=title_text, font=("Arial", 18, "bold"))
        label.pack(anchor="w")
        info = tk.Label(page, text=f"Эта страница: {name}", font=("Arial", 14))
        info.pack(anchor="w", pady=(8, 0))
        return page
    else:
        page = tk.Frame(content)
        return page
pages["home"] = create_page("home", "Главная")
pages["profile"] = create_page("profile", "Профиль")
pages["settings"] = create_page("settings", "Настройки")
pages["clicker"] = create_page()

def set_active_button(key):
    for k, btn in menu_buttons.items():
        if k == key:
            btn.config(relief="sunken")
        else:
            btn.config(relief="raised")


def show_page(key):
    for p in pages.values():
        p.pack_forget()
    pages[key].pack(fill="both", expand=True)
    set_active_button(key)

def add_menu_button(text, key):
    btn = tk.Button(sidebar, text=text, anchor="w", command=lambda: show_page(key))
    btn.pack(fill="x", pady=4)
    menu_buttons[key] = btn

add_menu_button("Главная", "home")
add_menu_button("Профиль", "profile")
add_menu_button("Настройки", "settings")
add_menu_button("Кликер", "clicker")
show_page("home")

home = tk.Frame(content)
tk.Label(home, text="Главная", font=("Arial", 24, "bold")).pack(anchor="w")
tk.Label(home, text="Добро пожаловать! Выберите раздел слева.", font=("Arial", 16)).pack(anchor="w", pady=(8, 0))
pages["home"] = home
profile = tk.Frame(content)
tk.Label(profile, text="Профиль", font=("Arial", 24, "bold")).pack(anchor="w")
tk.Label(profile, text="Добро пожаловать! Выберите раздел слева.", font=("Arial", 16)).pack(anchor="w", pady=(8, 0))
pages["profile"] = profile
settings = tk.Frame(content)
tk.Label(settings, text="Настройки", font=("Arial", 24, "bold")).pack(anchor="w")
tk.Label(settings, text="Добро пожаловать! Выберите раздел слева.", font=("Arial", 16)).pack(anchor="w", pady=(8, 0))
pages["settings"] = settings
clicker = tk.Frame(content)
tk.Label(clicker, text="Кликер", font=("Arial", 24, "bold")).pack(anchor="w")
tk.Label(clicker, text="Добро пожаловать! Выберите раздел слева или вы можете\nкликать xD", font=("Arial", 16)).pack(anchor="w", pady=(8, 0))
countClick = 0
message = tk.StringVar(value=f"Количество нажатий: {countClick}")

def button_Click():
    global countClick
    countClick += 1
    message.set(f"Количество нажатий: {countClick}")

tk.Label(clicker, textvariable=message, font=("Arial", 16, "bold")).pack(anchor="center", pady=(8, 0))
tk.Button(clicker, text="Клик", font=("Arial", 24), command=button_Click).pack(anchor="center", ipadx=10, ipady=10)
pages["clicker"] = clicker

root.mainloop()