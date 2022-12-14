import tkinter as tk
from tkinter import ttk

import pyperclip

from loguin import *

with open("data/data.json") as data:
    list_json = json.load(data)
wallet = Wallet(list_json)


class Gui:
    def __init__(self, master):
        """ used to make a new instance of the Gui class with all the inner-methods
        pre:
            :param master will be used as the root
        post: a new instance of Gui class is initiated
        external methods: add_record(),delete_record(),edit_record(),copy_password(),copy_user(),hide_password()
        """

        # Initiating the master settings window size and title

        master.title("Gestionnaire de mot de passe")
        master.minsize(750, 500)
        master.maxsize(750, 500)

        # setting the treeview structure

        colon = ("username", "password")
        self.treeview = ttk.Treeview(master, columns=colon,
                                     height=20)
        self.treeview.pack(padx=5, pady=5)

        self.treeview.heading("#0", text="Site Web")
        self.treeview.heading("username", text="Utilisateur")
        self.treeview.heading("password", text="Mot de passe")

        # setting the different buttons and their actions

        button1 = ttk.Button(master, text="Ajouter donnée", command=self.add_record)
        button1.pack(padx=5, pady=5, side=tk.RIGHT)

        button2 = ttk.Button(master, text="Effacer donnée", command=self.delete_record)
        button2.pack(padx=5, pady=5, side=tk.RIGHT)

        button3 = ttk.Button(master, text="Editer mot de passe", command=self.edit_record)
        button3.pack(padx=5, pady=5, side=tk.RIGHT)

        button4 = ttk.Button(master, text="Copier mot de passe", command=self.copy_password)
        button4.pack(padx=5, pady=5, side=tk.RIGHT)

        button5 = ttk.Button(master, text="Copier utilisateur", command=self.copy_user)
        button5.pack(padx=5, pady=5, side=tk.RIGHT)

        self.v = tk.IntVar()
        x = ttk.Checkbutton(master, text="Afficher les mots de passes", variable=self.v, onvalue=1,
                            offvalue=0, command=self.hide_password)
        self.v.set(0)
        x.pack(padx=5, pady=5, side=tk.RIGHT)

        # at the beginning all the password are hided

        self.hide_password()

    def delete_record(self):
        """ delete a specified row in the GUI/ json
        pre: none
        post: the selected row has been deleted from the GUI and json
        raise: you must select something by clicking on it to remove it
        external call: wallet.delete_site_password(),clear_all(), wallet.save_wallet(),hide_password()
        """
        x = self.treeview.focus()
        if x:
            for record in x:
                self.treeview.delete(record)
                wallet.delete_site_password(int(record) - 1)
                self.clear_all()
                save_wallet(wallet.wallet)
                self.hide_password()
        else:
            messagebox.showerror(title="Erreur", message="Selectionnez une ligne svp")
            raise (TypeError, "Nothing selected.")

    def clear_all(self):
        """empty all the treeview content
        pre: none
        post: all the rows in the treeview has been removed

        """
        for item in self.treeview.get_children():
            self.treeview.delete(item)

    def add_record(self):
        """ ad a new record
        pre: none
        post:add a new row in the treeview and the json
        external methods:website.Website(),username.Username(),wallet.Wallet.add_new_logs(),wallet.save_wallet(),
                         clear_all(),hide_password(),ask_auto_password()
        """

        site = ""
        while site == "":
            site = simpledialog.askstring("Input", "Entrer le nom du site")
        name = ""
        while name == "":
            name = simpledialog.askstring("Input", "Entrer nom d'utilisateur")

        website_obj = Website(site)
        username_obj = Username(name)
        password_obj = self.ask_auto_password()
        wallet.add_new_logs(website_obj, username_obj, password_obj)
        save_wallet(wallet.wallet)
        self.clear_all()
        self.hide_password()

    @staticmethod
    def ask_auto_password():
        """ create a new password
        pre: none
        post: create a (auto) password
        external_methods:random_password.automatic_random_password(),password.testing_password()
        """
        new_password = ""
        while new_password == "":
            new_password = simpledialog.askstring("Input", "Entrer votre mot de passe "
                                                           "(si vous voulez un mot de passe automatique entrer Y)")
        if new_password.lower() == "y":
            new_password = random_passWord.automatic_random_password()
        password_obj = Password(new_password)
        testing_password = password_obj.testing_password(
            password_obj.password)  # test the len / 1 letter 1 number and 1 alnum
        if testing_password == 0:
            messagebox.showwarning(title="Attention", message="Mot de passe faible pensez à changer")
        return password_obj

    def edit_record(self):
        """
        pre: you must have the data/data.json
        post: the specified line is edited
        raise: you must select a line to edit
        external_methods:wallet.Wallet.edit_site_password(),wallet.save_wallet()
        """
        y = self.treeview.focus()
        if y:
            password_obj = self.ask_auto_password()
            wallet.edit_site_password(y, password_obj)
            save_wallet(wallet.wallet)
            self.clear_all()
            self.hide_password()
        else:
            messagebox.showerror(title="Erreur", message="Selectionnez une ligne svp")
            raise (TypeError, "Nothing selected.")

    def hide_password(self):
        """
        pre:
            you must have the data/data.json
        post: all the password will be shown as *********
        """
        if self.v.get():
            self.clear_all()
            with open("data/data.json", "r") as file:
                jjson = json.load(file)

            for line in range(len(jjson)):
                self.treeview.insert("", tk.END, iid=str(line + 1), text=jjson[line]["site"],
                                     values=(jjson[line]["id"], jjson[line]["password"]))
        else:
            self.clear_all()
            with open("data/data.json", "r") as file:
                jjson = json.load(file)

            for line in range(len(jjson)):
                self.treeview.insert("", tk.END, iid=str(line + 1), text=jjson[line]["site"],
                                     values=(jjson[line]["id"], "*********"))

    def copy_password(self):
        """
        pre: you must import pyperclip
        post: the selected password will be copied in your clipboard
        raise: you must select a row before copying
        """
        y = self.treeview.focus()
        if y:
            pyperclip.copy(wallet.wallet[int(y) - 1]["password"])
        else:
            messagebox.showerror(title="Erreur", message="Selectionnez une ligne svp")
            raise (TypeError, "Nothing selected.")

    def copy_user(self):
        """
        pre:you must import pyperclip
        post: the selected user  will be copied in your clipboard
        raise: you must select a row before copying
        """
        y = self.treeview.focus()
        if y:
            pyperclip.copy(wallet.wallet[int(y) - 1]["id"])
        else:
            messagebox.showerror(title="Erreur", message="Selectionnez une ligne svp")
            raise (TypeError, "Nothing selected.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestionnaire de mot de passe")
    loguin = LogGuiIn()
    root.destroy()
    root = tk.Tk()
    gui = Gui(root)
    root.mainloop()
