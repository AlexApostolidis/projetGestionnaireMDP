import random_passWord
from loguin import *
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from classes import *
import pyperclip

with open("data.json") as data:
    list_json = json.load(data)
wallet = Wallet(list_json)


def save_wallet(data_saving):
    """
        save list in a JSON file
        param: none
        return: none
    """
    with open('data.json', 'w') as file:
        json.dump(data_saving, file)


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

        button = ttk.Button(master, text="Copier le mot de passe", command=self.copy_password)
        button.pack(padx=5, pady=5, side=tk.RIGHT)

        button = ttk.Button(master, text="Copier l'utilisateur", command=self.copy_user)
        button.pack(padx=5, pady=5, side=tk.RIGHT)

        self.v = tk.IntVar()
        x = ttk.Checkbutton(master, text="Afficher les mots de passes", variable=self.v, onvalue=1,
                            offvalue=0, command=self.hide_password)
        self.v.set(0)
        x.pack(padx=5, pady=5, side=tk.RIGHT)

        """scroll = ttk.Scrollbar(master, orient="vertical", command=self.treeview.yview)
        # scroll.pack(side = 'right', fill = 'y')

        self.treeview.configure(yscrollcommand=scroll.set)"""

        self.hide_password()

    def delete_record(self):
        x = self.treeview.focus()
        if x:
            if len(wallet) < 1:
                messagebox.showerror(title="Erreur", message="Votre fichier est vide")

            for record in x:
                self.treeview.delete(record)
                wallet.delete_site_password(int(record) - 1)
                self.clear_all()
                save_wallet(wallet.wallet)
                self.hide_password()
        else:
            messagebox.showerror(title="Erreur", message="Selectionnez une ligne svp")

    def clear_all(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

    def add_record(self):
        parent = simpledialog.askstring("Input", "Entrer le nom du site")
        name = simpledialog.askstring("Input", "Entrer nom d'utilisateur")

        # self.treeview.insert(parent, tk.END, text=name, values=(name, password))

        website_obj = Website(parent)
        username_obj = Username(name)

        new_password = simpledialog.askstring("Input", "Entrer votre mot de passe "
                                                       "(si vous voulez un mot de passe automatique entrer Y)")

        if new_password.lower() == "y":
            new_password = random_passWord.automatic_random_password()
        password_obj = Password(new_password)
        testing_password = password_obj.testing_password(password_obj.password)
        if testing_password == 0:
            messagebox.showwarning(title="Attention", message="Mot de passe faible pensez à changer")

        wallet.add_new_logs(website_obj, username_obj, password_obj)
        save_wallet(wallet.wallet)
        self.clear_all()
        self.hide_password()

    def edit_record(self):
        y = self.treeview.focus()
        if y:
            if len(wallet) < 1:
                messagebox.showerror(title="Erreur", message="Votre fichier est vide")
            else:
                new_password = simpledialog.askstring("Input", "Entrer votre mot de passe "
                                                               "(si vous voulez un mot de passe automatique entrer Y")
                if new_password.lower() == "y":
                    new_password = random_passWord.automatic_random_password()
                password_obj = Password(new_password)
                testing_password = password_obj.testing_password(password_obj.password)
                if testing_password == 0:
                    messagebox.showwarning(title="Attention", message="Mot de passe faible pensez à changer")
                wallet.edit_site_password(y, password_obj.password)

                save_wallet(wallet.wallet)
                self.clear_all()
                self.hide_password()
        else:
            messagebox.showerror(title="Erreur", message="Selectionnez une ligne svp")

    def hide_password(self):
        if self.v.get():
            self.clear_all()
            file = open("data.json", "r")
            jjson = json.load(file)

            for line in range(len(jjson)):
                self.treeview.insert("", tk.END, iid=str(line + 1), text=jjson[line]["site"],
                                     values=(jjson[line]["id"], jjson[line]["password"]))
        else:
            self.clear_all()
            file = open("data.json", "r")
            jjson = json.load(file)

            for line in range(len(jjson)):
                self.treeview.insert("", tk.END, iid=str(line + 1), text=jjson[line]["site"],
                                     values=(jjson[line]["id"], "*********"))

    def copy_password(self):
        y = self.treeview.focus()
        if y:

            pyperclip.copy(wallet.wallet[int(y) - 1]["password"])
        else:
            messagebox.showerror(title="Erreur", message="Selectionnez une ligne svp")

    def copy_user(self):
        y = self.treeview.focus()
        if y:

            pyperclip.copy(wallet.wallet[int(y) - 1]["id"])
        else:
            messagebox.showerror(title="Erreur", message="Selectionnez une ligne svp")


if __name__ == "__main__":
    root = tk.Tk()

    root.title("Gestionnaire de mot de passe")
    loguin = LogGuiIn()
    root.destroy()
    root = tk.Tk()
    gui = Gui(root)

    root.mainloop()
