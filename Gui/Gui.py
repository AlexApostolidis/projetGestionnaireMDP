#"""
from tkinter import *
from tkinter import ttk
import json

def afficher():
    print("i")
data = [ ["val1", "val2", "val3"], #lorem ipsum pour remplir le tableau
         ["asd1", "asd2", "asd3"],
         ["bbb1", "bbb3", "bbb4"],
         ["ccc1", "ccc3", "ccc4"],
         ["ddd1", "ddd3", "ddd4"],
         ["eee1", "eee3", "eee4"] ]



root = Tk()  # create root window
root.title("Gestionnaire de mot de passe")  # title of the GUI window
root.minsize(900, 600)
root.maxsize(900, 600)  # specify the max size the window can expand to
#root.geometry("900x600") #specify the max space the root can take on the window in pixels
root.config(bg="#AFAFAF")  # specify background color

# Create left and right frames
left_frame = Frame(root, width=200, height=600, bg='#303030')
left_frame.grid(row=0, column=0, padx=10, pady=5,rowspan=10,sticky='ns')

right_frame = Frame(root, width=850, height=600, bg='#303030')
right_frame.grid(row=0, column=1, padx=10, pady=5,sticky='ns')

# Create frames and labels in left_frame
Label(left_frame, text="Site Web").grid(row=0, column=0, padx=5, pady=5)

# Create tool bar frame inside left_frame
tool_bar = Frame(left_frame, width=180, height=185,bg="#303030")
tool_bar.grid(row=1, column=0, padx=5, pady=5)



# Example labels that could be displayed under the "Tool" menu
Bouton1 = Button(tool_bar,text="Ajouter entrée",command=afficher,bg="#AFAFAF")
Bouton1.grid(row=2, column=0)
Bouton2 = Button(tool_bar,text="Modifier entrée",command=afficher,bg="#AFAFAF")
Bouton2.grid(row=3, column=0, padx=5, pady=5)
Bouton3 = Button(tool_bar,text="Supprimer entrée",command=afficher,bg="#AFAFAF")
Bouton3.grid(row=4, column=0, padx=5, pady=5)
Bouton4 = Button(tool_bar,text="Afficher toutes les entrées",command=afficher,bg="#AFAFAF")
Bouton4.grid(row=5, column=0, padx=5, pady=5)

#printing the JSON content as rows of a new frame inside right_frame

upper_right_frame = Frame(right_frame,width=630,height=150,bg="#303030")
upper_right_frame.grid(row=0, column=0, padx=10, pady=5,sticky='ns')
Label(upper_right_frame, text="Site Web\t\t\t\t").grid(row=0, column=1)
Label(upper_right_frame, text="Nom d'utilisateur\t\t\t\t").grid(row=0, column=2)
Label(upper_right_frame, text="Mot de passe\t\t\t\t").grid(row=0, column=3)

lower_right_frame = Frame(right_frame,width=630,height=800,bg="#303030")
lower_right_frame.grid(row=0, column=1, padx=10, pady=5,sticky='ns')


tree = ttk.Treeview(lower_right_frame, columns = (1,2,3), height = len(data), show = "headings")
tree.pack(side = 'left')

tree.heading(1, text="Site Web")
tree.heading(2, text="Nom d'utilisateur")
tree.heading(3, text="Mot de passe")

tree.column(1, width = 250)
tree.column(2, width = 250)
tree.column(3, width = 250)

scroll = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
#scroll.pack(side = 'right', fill = 'y')

tree.configure(yscrollcommand=scroll.set)



for val in data:
    tree.insert('', 'end', values = (val[0], val[1], val[2]) )




root.mainloop()
"""
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x200")

data = [ ["val1", "val2", "val3"],
         ["asd1", "asd2", "asd3"],
         ["bbb1", "bbb3", "bbb4"],
         ["ccc1", "ccc3", "ccc4"],
         ["ddd1", "ddd3", "ddd4"],
         ["eee1", "eee3", "eee4"] ]


frame = Frame(root)
frame.pack()

tree = ttk.Treeview(frame, columns = (1,2,3), height = 5, show = "headings")
tree.pack(side = 'left')

tree.heading(1, text="Column 1")
tree.heading(2, text="Column 2")
tree.heading(3, text="Column 3")

tree.column(1, width = 100)
tree.column(2, width = 100)
tree.column(3, width = 100)

scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side = 'right', fill = 'y')

tree.configure(yscrollcommand=scroll.set)

for val in data:
    tree.insert('', 'end', values = (val[0], val[1], val[2]) )

root.mainloop()
"""