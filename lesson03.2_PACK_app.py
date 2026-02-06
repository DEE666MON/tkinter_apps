import tkinter as tk

root = tk.Tk()
root.title("Tkinter PACK")
window_w, window_h = 800, 400
screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (screen_w - window_w) // 2, (screen_h - window_h) // 2
root.geometry(f"{window_w}x{window_h}+{x}+{y}")
root.resizable(False, False)
tk.Label(root, text="Верх", font=("Arial", 18)).pack(pady=10)
tk.Label(root, text="Низ", font=("Arial", 18)).pack(side="bottom", pady=10)
tk.Button(root, text="Слева").pack(side="left", padx=10, pady=10, fill="y")
tk.Button(root, text="Справа").pack(side="right", padx=10, pady=10, fill="y")
tk.Button(root, text="Низ").pack(side="bottom", padx=10, pady=10, fill="y")
root.mainloop()