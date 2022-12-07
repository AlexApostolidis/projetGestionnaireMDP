import json
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog

import random_passWord
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

        self.read_data()

    def read_data(self):
        file = open("data.json", "r")
        jjson = json.load(file)


        for line in jjson:
            self.treeview.insert("", tk.END, text=line["site"], values=(line["id"], line["password"]))

    def delete_record(self):
        """row_id = self.treeview.focus()

        if row_id != "":
            self.treeview.delete(row_id)
        print(row_id)
        index_Json = int(row_id[1:], base=16) - 1
        #print(index_Json)
        self.selectItem(index_Json)


        wallet.delete_site_password(index_Json)
        wallet.save_wallet()
        self.clear_all()
        self.read_data()"""
        x = self.treeview.selection()
        index_Json = int(x[1:], base=16) - 1
        for record in index_Json:
            self.treeview.delete(record)
            wallet.delete_site_password(record)
            wallet.save_wallet()
            self.clear_all()
            self.read_data()

    def selectItem(self,a):
        curItem = self.treeview.focus()
        print(self.treeview.item(curItem))


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

        wallet.add_new_logs(website_obj, username_obj, password_obj)
        wallet.save_wallet()
        self.clear_all()
        self.read_data()


root = tk.Tk()
root.title("Gestionnaire de mot de passe")
gui = Gui(root)
root.mainloop()
