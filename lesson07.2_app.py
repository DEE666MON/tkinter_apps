import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__
        self.title("Приложение авторизации")
        self.geometry("400x250")
        self.resizable(False, False)
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        self.frames = {}
        for F in (LoginFrame, RegisterFrame, MainFrame):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("LoginFrame")
    def show_frame(self, name: str):
        self.frames[name].tkraise()

class LoginFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        tk.Label(self, text="Экран: Вход", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Перейти к регистрации", command=lambda: app.show_frame("RegisterFrame")).pack(pady=10)
        tk.Button(self, text="Войти", command=lambda: app.show_frame("MainFrame")).pack(pady=10)

class RegisterFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        tk.Label(self, text="Экран: Регистрации", font=("Arial", 16)).pack(pady=20)
        # tk.Button(self, text="Вернуться ко входу", command=).pack(pady=10)
        # tk.Button(self, text="Регистрация", command=).pack(pady=10)

class MainFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        tk.Label(self, text="Экран: Главная", font=("Arial", 16)).pack(pady=20)
        # tk.Button(self, text="Выйти", command=).pack(pady=10)

if __name__ == "__main__":
    App().mainloop()