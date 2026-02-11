import tkinter as tk
import sqlite3

root = tk.Tk()
root.title("Tkinter приложение регистрации/авторизации с БД")
window_w, window_h = 600, 400
screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (screen_w - window_w) // 2, (screen_h - window_h) // 2
root.geometry(f"{window_w}x{window_h}+{x}+{y}")
root.resizable(False, False)
regOrLogFlag = True

def get_db_connection():
    conn = sqlite3.connect("lesson07_database.db")
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    conn = get_db_connection()
    conn.execute("""
                CREATE TABLE IF NOT EXISTS Users (
                idUser INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
                )""")
    conn.commit()
    conn.close()
def regOrLogQuestion():
    global regOrLogFlag, m1, m4, m5, m6
    if(regOrLogFlag):
        m1.set("Авторизация")
        m4.set("Войти")
        m5.set("Вы ещё не зарегестрированы? Нажмите кнопку ниже.")
        m6.set("Зарегистрироваться")
        m7.set("")
        regOrLogFlag = False
    else:
        m1.set("Регистрация")
        m4.set("Зарегистрироваться")
        m5.set("Вы уже зарегестрированы? Нажмите кнопку ниже.")
        m6.set("Войти")
        m7.set("")
        regOrLogFlag = True
def regOrLogLogic():
    global regOrLogFlag, ent_log, ent_pass, m1, m7
    login = ent_log.get().strip()
    password = ent_pass.get().strip()
    if (not len(login) or not len(password)):
        m7.set("Ошибка! Нужно заполнить всё поля.")
        return
    if (regOrLogFlag):
        conn = get_db_connection()
        question = conn.execute("SELECT idUser FROM users WHERE login = ?", (login,)).fetchone()
        if question:
            m7.set("Ошибка! Пользователь с таким именем уже существует.")
        else:
            conn.execute("INSERT INTO users (login, password) VALUES (?, ?)",(login, password))
            conn.commit()
            m1.set("Успешная регистрация аккаунта.")
            m7.set("")
    else:
        conn = get_db_connection()
        question = conn.execute("SELECT * FROM Users WHERE login = ? and password = ?", (login, password)).fetchone()
        if not question:
            m7.set("Ошибка! Не правильный логин или пароль.")
        else:
            m1.set("Успешный вход в аккаунт.")
            m7.set("")
    conn.close()

init_db()
area1 = tk.Frame(root)
area1.pack(fill="x")
area2 = tk.Frame(root)
area2.pack(fill="y", expand=True)
area3 = tk.Frame(root)
area3.pack(fill="both", expand=True)
m1 = tk.StringVar(value="Регистрация")
m2 = tk.StringVar(value="Логин: ")
m3 = tk.StringVar(value="Пароль: ")
m4 = tk.StringVar(value="Зарегистрироваться")
m5 = tk.StringVar(value="Вы уже зарегестрированы? Нажмите кнопку ниже.")
m6 = tk.StringVar(value="Войти")
m7 = tk.StringVar(value="")
tk.Label(area1, textvariable=m1, font=("Arial", 24, "bold")).pack(anchor="center", pady=(50, 10))
lbl_log = tk.Label(area2, textvariable=m2, font=("Arial", 16))
ent_log = tk.Entry(area2, font=("Arial", 16))
lbl_pass = tk.Label(area2, textvariable=m3, font=("Arial", 16))
ent_pass = tk.Entry(area2, font=("Arial", 16))
btn_regOrLog = tk.Button(area3, textvariable=m4, command=regOrLogLogic, font=("Arial", 16))
lbl_regOrLog = tk.Label(area3, textvariable=m5, font=("Arial", 12))
btn_regOrLogQuestion = tk.Button(area3, textvariable=m6, command=regOrLogQuestion, font=("Arial", 12))
lbl_Error = tk.Label(area3, textvariable=m7, font=("Arial", 12), foreground="red")
lbl_log.grid(row=0, column=0, sticky="w", pady=(0, 10))
ent_log.grid(row=0, column=1, sticky="ew", pady=(0, 10))
lbl_pass.grid(row=1, column=0, sticky="w", pady=(0, 10))
ent_pass.grid(row=1, column=1, sticky="ew")
btn_regOrLog.pack(anchor="center", padx=10, pady=10, ipadx=5, ipady=5)
lbl_regOrLog.pack(anchor="center", padx=(0, 10), pady=5)
btn_regOrLogQuestion.pack(anchor="center", padx=(0, 10), pady=5)
lbl_Error.pack(anchor="center")

root.mainloop()