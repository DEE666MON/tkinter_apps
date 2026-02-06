import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.title("Tkinter app2")
window_w, window_h = 900, 520
screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (screen_w - window_w) // 2, (screen_h - window_h) // 2
root.geometry(f"{window_w}x{window_h}+{x}+{y}")
root.resizable(False, False)

app = tk.Frame(root)
app.pack(fill="both", expand=True)
leftBar = tk.Frame(app, width=200)
leftBar.pack(side="left", fill="y")
leftBar.pack_propagate(False)
rightContent = tk.Frame(app)
rightContent.pack(side="left", fill="both", expand=True, padx=5)
flagBtnC = False
flagBtnS = False
contacts = [{"name": "Дмитрий", "phone": "89008007060", "city": "СТАРЫЙ ОСКОЛ"},
            {"name": "Равиль", "phone": "88005553535", "city": "СТАРЫЙ ОСКОЛ"},
            {"name": "Александр", "phone": "1234567890", "city": "МОСКВА"},
            {"name": "Юра", "phone": "0987654321", "city": "САНКТ-ПЕТЕРБУРГ"}]
m1 = tk.StringVar(value="Контакты")
m2 = tk.StringVar(value="Имя: ")
m3 = tk.StringVar(value="Телефон: ")
m4 = tk.StringVar(value="Город: ")
tk.Label(rightContent, textvariable=m1, font=("Arial", 24, "bold")).pack(anchor="center", pady=10)
tk.Label(rightContent, textvariable=m2, font=("Arial", 18)).pack(anchor="w", pady=2)
tk.Label(rightContent, textvariable=m3, font=("Arial", 18)).pack(anchor="w", pady=2)
tk.Label(rightContent, textvariable=m4, font=("Arial", 18)).pack(anchor="w", pady=2)
contactsListboxFrame = tk.Frame(rightContent)
contactsListboxFrame.pack(fill="both", expand=True, padx=10, pady=10)
scrollbar = tk.Scrollbar(contactsListboxFrame)
scrollbar.pack(side="right", fill="y")
contactListbox = tk.Listbox(contactsListboxFrame, yscrollcommand=scrollbar.set, font=("Arial", 14), selectmode="single")
contactListbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=contactListbox.yview)

def contactsAdd_Click():
    name = simpledialog.askstring("Добавить контакт", "Введите имя:")
    phone = simpledialog.askstring("Добавить контакт", "Введите телефон:")
    city = simpledialog.askstring("Добавить контакт", "Введите город:")
    if not name or not phone or not city:
        return
    new_contact = {
        "name": name,
        "phone": phone,
        "city": city.upper()
    }
    contacts.append(new_contact)
    update_contact_list()
def contactsDelete():
    selection = contactListbox.curselection()
    if not selection:
        messagebox.showwarning("Внимание", "Выберите контакт для удаления!")
        return
    index = selection[0]
    contact_to_delete = contacts[index]
    confirm = messagebox.askyesno("Подтверждение удаления", f"Вы действительно хотите удалить контакт:\n{contact_to_delete['name']}?")
    if confirm:
        contacts.pop(index)
        contactsClearInfo_Click()
def contactsClearInfo_Click():
        m1.set("Контакты")
        m2.set("Имя: ")
        m3.set("Телефон: ")
        m4.set("Город: ")
        contactListbox.selection_clear(0, tk.END)
        contactsListboxFrame.pack_forget()
        contactsBtnsFrame.pack_forget()
        contactsListboxFrame.pack(fill="both", expand=True, padx=10, pady=10)
        contactsBtnsFrame.pack(fill="x", padx=10, pady=10)
        update_contact_list()
def update_contact_list():
    contactListbox.delete(0, tk.END)
    for contact in contacts:
        display_text = f"{contact['name']} - {contact['phone']} - {contact['city']}"
        contactListbox.insert(tk.END, display_text)
def on_contact_select(event=None):
    selection = contactListbox.curselection()
    if selection:
        index = selection[0]
        if index < len(contacts):
            contact = contacts[index]
            m2.set(f"Имя: {contact['name']}")
            m3.set(f"Телефон: {contact['phone']}")
            m4.set(f"Город: {contact['city']}")
def mainContactsBtn_Click():
    global flagBtnC, flagBtnS
    if not flagBtnC:
        m1.set("Контакты")
        m2.set("Имя: ")
        m3.set("Телефон: ")
        m4.set("Город: ")
        contactsListboxFrame.pack(fill="both", expand=True, padx=10, pady=10)
        contactsBtnsFrame.pack(fill="x", padx=10, pady=10)
        update_contact_list()
        flagBtnC = True
        flagBtnS = False
def uniqueCities(flag = True):
    listUC = []
    if flag:
        for c in contacts:
            for k, v in c.items():
                if k == "city" and v not in listUC:
                    listUC.append(v)
        return len(listUC)
    else:
        for c in contacts:
            for k, v in c.items():
                if k == "city" and v not in listUC:
                    listUC.append(v)
        return listUC
def manyCountCity():
    city_count = {}
    for contact in contacts:
        city = contact["city"]
        if city in city_count:
            city_count[city] += 1
        else:
            city_count[city] = 1
    max_count = 0
    most_common_city = None
    for city, count in city_count.items():
        if count > max_count:
            max_count = count
            most_common_city = city
        elif count == max_count:
            most_common_city = f"{most_common_city}, {city}"
    return most_common_city
def mainStatisticBtn_Click():
    global flagBtnC, flagBtnS
    rightContent.grid_remove()
    if not flagBtnS:
        m1.set("Статистика")
        m2.set(f"Количество контактов: {len(contacts) or "нет"}")
        m3.set(f"Количество уникальных городов: {uniqueCities() or "нет"}")
        m4.set(f"Самый частый город: {manyCountCity() or "нет"}")
        contactsListboxFrame.pack_forget()
        contactsBtnsFrame.pack_forget()
        flagBtnS = True
        flagBtnC = False

def mainExitBtn_Click(event=None):
    root.destroy()

contactsBtnsFrame = tk.Frame(rightContent)
contactsBtnsFrame.pack(fill="x", padx=10, pady=10)
tk.Button(contactsBtnsFrame, text="Добавить", command=contactsAdd_Click, font=("Arial", 18)).pack(side="left", padx=(0, 5))
tk.Button(contactsBtnsFrame, text="Удалить", command=contactsDelete, font=("Arial", 18)).pack(side="left", padx=(0, 5))
tk.Button(contactsBtnsFrame, text="Очистить", command=contactsClearInfo_Click, font=("Arial", 18)).pack(side="left")
tk.Button(leftBar, text="Контакты", command=mainContactsBtn_Click, font=("Arial", 18, "bold")).pack(anchor="center", fill="both", pady=(0, 5))
tk.Button(leftBar, text="Статистика", command=mainStatisticBtn_Click, font=("Arial", 18, "bold")).pack(anchor="center", fill="both", pady=(0, 5))
tk.Button(leftBar, text="Выход", command=mainExitBtn_Click, font=("Arial", 18, "bold")).pack(anchor="center", fill="both")

update_contact_list()
contactListbox.bind('<<ListboxSelect>>', on_contact_select)
root.bind("<Escape>", mainExitBtn_Click)
root.mainloop()