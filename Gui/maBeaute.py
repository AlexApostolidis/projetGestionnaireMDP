import random_passWord
from loguin import *
import json
import tkinter as tk
from tkinter import  ttk
from tkinter import messagebox
from tkinter import simpledialog
from classes import *

wallet = Wallet()
data = wallet.opening_json()


class Gui:
    def __init__(self, master):

        colon = ("username", "password")
        self.treeview = ttk.Treeview(master, columns=colon,
                                     height=20)  # on peut mettre une hauteur dynamique sur len(json)
        self.treeview.pack(padx=5, pady=5)

        self.treeview.heading("#0", text="Site Web")
        self.treeview.heading("username", text="Utilisateur")
        self.treeview.heading("password", text="Mot de passe")

        button = ttk.Button(master, text="Ajouter donnée", command=self.add_record)
        button.pack(padx=5, pady=5, side=tk.RIGHT)

        button = ttk.Button(master, text="Effacer donnée", command=self.delete_record)
        button.pack(padx=5, pady=5, side=tk.RIGHT)

        button = ttk.Button(master, text="Editer mot de passe", command=self.edit_record)
        button.pack(padx=5, pady=5, side=tk.RIGHT)

        """scroll = ttk.Scrollbar(master, orient="vertical", command=self.treeview.yview)
        # scroll.pack(side = 'right', fill = 'y')

        self.treeview.configure(yscrollcommand=scroll.set)"""

        self.read_data()

    def read_data(self):
        self.clear_all()
        file = open("data.json", "r")
        jjson = json.load(file)

        for line in range(len(jjson)):
            self.treeview.insert("", tk.END, iid=line + 1, text=jjson[line]["site"],
                                 values=(jjson[line]["id"], jjson[line]["password"]))

    def delete_record(self):
        x = self.treeview.focus()
        if len(wallet) < 1:
            messagebox.showerror(title="Erreur", message="ptn zbi")

        for record in x:
            self.treeview.delete(record)
            wallet.delete_site_password(int(record) - 1)
            self.clear_all()
            self.read_data()

    def clear_all(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

    def add_record(self):
        parent = simpledialog.askstring("Input", "Entrer parent (si existe)")
        name = simpledialog.askstring("Input", "Entrer nom d'utilisateur")

        # self.treeview.insert(parent, tk.END, text=name, values=(name, password))

        website_obj = Website(parent)
        username_obj = Username(name)
        selected_item = self.treeview.selection()[0:]

        password = simpledialog.askstring("Input", "mdp auto taper Y")

        if password == "Y":
            password = random_passWord.automatic_random_password()
        password_obj = Password(password)
        testing_password = password_obj.testing_password(password_obj.password)
        if testing_password == 0:
            messagebox.showwarning(title="Attention", message="Mot de passe faible pensez à changer")

        wallet.add_new_logs(website_obj, username_obj, password_obj)
        wallet.save_wallet()
        self.clear_all()
        self.read_data()

    def edit_record(self):
        y = self.treeview.focus()
        if len(wallet) < 1:
            messagebox.showerror(title="Erreur", message="ptn zbi")
        else:
            password = simpledialog.askstring("Input", "mdp auto taper Y")

            if password == "Y":
                password = random_passWord.automatic_random_password()
            password_obj = Password(password)
            testing_password = password_obj.testing_password(password_obj.password)
            if testing_password == 0:
                messagebox.showwarning(title="Attention", message="Mot de passe faible pensez à changer")

            wallet.edit_site_password(y, password)

            wallet.save_wallet()
            self.clear_all()
            self.read_data()


root = tk.Tk()

root.title("Gestionnaire de mot de passe")
loguin = Loguin(root)
root.destroy()
root = tk.Tk()
gui = Gui(root)

root.mainloop()
