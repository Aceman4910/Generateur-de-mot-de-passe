"""
Generation automatique de mot de passe pour l'utilisateur

"""

# On importe Tkinter
from tkinter import *
#import de la boite de massage
from tkinter import messagebox
#import de la date du jour
import time

# definition des variable
class MdpSolu:

        def __init__(self):
                # Definition de la date du jours
                
                jours = time.strftime('%d')
                mois = time.strftime('%m')
                annee = time.strftime ('%Y')
                #cacul de la date du jours
                self.DateDay = (jours+mois+annee).encode('utf-8')

        def Calcul(self,userstr,DateNaissstr,Entreprisestr,Deptstr):
                #transfortion des variable et UTF-8
                User = userstr.encode('utf-8')

                DateNaiss = DateNaissstr.encode('utf-8')

                Entreprise = Entreprisestr.encode('utf-8')

                Dept =Deptstr.encode('utf-8')

                #calcul du mot de passe 
                PwHex=hex(int(DateNaiss.hex(),16)^int(Entreprise.hex(),16)^int(self.DateDay.hex(),16))+Dept.hex()

                #passage en format UTF-8
                PwUTF= PwHex[2:]

                #reformation du mot de passe
                self.PwFinal = bytes.fromhex(PwUTF).decode('utf-8',"ignore")
		
# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# interface racine
champ_label = Label(fenetre, text="Génération du mot de passe!")
# On affiche le label dans la fenêtre
champ_label.pack()
# interface racine
champ_label = Label(fenetre, text="ID User")
# On affiche le label dans la fenêtre
champ_label.pack()
#Recuperation de IDuser
var_ID_User = StringVar()
ID_User = Entry(fenetre, textvariable=var_ID_User, width=20)
ID_User.pack()
# interface racine
champ_label = Label(fenetre, text="Date de Naissance")
champ_label.pack()
champ_label = Label(fenetre,fg="red",text="Format (JJ/MM/AAAA)")
# On affiche le label dans la fenêtre
champ_label.pack()
#Recuperation de la date de naissance
var_Date_Naiss = StringVar()
Date_Naiss = Entry(fenetre, textvariable=var_Date_Naiss, width=10)
Date_Naiss.pack()
# interface racine
champ_label = Label(fenetre, text="Non de l'Entreprise ")
# On affiche le label dans la fenêtre
champ_label.pack()
#Recuperation du nom de l entreprise
var_Entreprise = StringVar()
Entreprise = Entry(fenetre, textvariable=var_Entreprise, width=20)
Entreprise.pack()
# interface racine
champ_label = Label(fenetre, text="Département du Siège")
# On affiche le label dans la fenêtre
champ_label.pack()
#Recuperation de code postal
var_Dept_Siege = StringVar()
Code_Postal = Entry(fenetre, textvariable=var_Dept_Siege, width=5)
Code_Postal.pack()

# bouton Generation du mot de passe

def GeneApp():
	#recuparation des variable entrer
	Valeur_ID_User = var_ID_User.get()
	Valeur_Date_Naiss = var_Date_Naiss.get()
	Valeur_Entreprise = var_Entreprise.get()
	Valeur_Dept_Siege = var_Dept_Siege.get()
	
	User = "%s"%(Valeur_ID_User)

	DateNaiss = "%s"%(Valeur_Date_Naiss)

	Entreprise = "%s"%(Valeur_Entreprise)

	Dept ="%s"%(Valeur_Dept_Siege)

	#initialisation de generateur de mot de passe
	PwGene = MdpSolu()
	#calcul du mot de passe
	PwGene.Calcul(User,DateNaiss,Entreprise,Dept)
	#vidage de presse-papier
	fenetre.clipboard_clear()
	#récuperation du mot de passe
	MDpFinal = PwGene.PwFinal
	#copie du mot de passe dans la presse-papier
	fenetre.clipboard_append(MDpFinal)
	
	#affichage du mot de passe
	MsgBox = messagebox.showinfo("Mot de Passe du Jour","le mot de passe "+MDpFinal+" a été copier dans le presse-papier")

bouton_quitter = Button(fenetre, text="Génération", command=GeneApp)
bouton_quitter.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()

"""
    Copyright (C) <2021> <Rascalou> <Yohann>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
	"""
