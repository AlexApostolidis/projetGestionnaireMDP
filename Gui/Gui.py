from tkinter import *

def afficher():
    print("i")

root = Tk()  # create root window
root.title("Gestionnaire de mot de passe")  # title of the GUI window
root.minsize(900, 600)
root.maxsize(900, 600)  # specify the max size the window can expand to
root.config(bg="#AFAFAF")  # specify background color

# Create left and right frames
upper_left_frame = Frame(root, width=200, height=50,bg='#303030')
#upper_left_frame.grid(row=0,column=0,padx=10, pady=5,sticky='n')

left_frame = Frame(root, width=200, height=400, bg='#303030')
left_frame.grid(row=0, column=0, padx=10, pady=5,rowspan=10,sticky='ns')

right_frame = Frame(root, width=850, height=600, bg='#303030')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# Create frames and labels in left_frame
Label(left_frame, text="Site Web").grid(row=0, column=0, padx=5, pady=5)

# Create tool bar frame
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



root.mainloop()
