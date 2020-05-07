from tkinter import *

mafenetre = Tk()
mafenetre.title("Nword")
mafenetre.iconbitmap("Nicon.ico")
mafenetre.geometry("600x500")
mafenetre.resizable(width=FALSE, height=FALSE)
temp_img = PhotoImage(file='dragon.png')
can = Canvas(mafenetre, width=600, height=500)
can.pack()
can.create_image(300, 250, image=temp_img)

def entrer_dico():

    profil = []
    profilYO = {}
    profilBirth = []
    loop = 0
    if EntreName.get() != "":
        profil.append(EntreName.get())
    if EntreLast_Name.get() != "":
        profil.append(EntreLast_Name.get())
    if EntreNickname.get() != "":
        profil.append(EntreNickname.get())
    if len(Entrebirth.get()) == 8:
        profilYO['birth']=Entrebirth.get()
    #-------------------------------------------------------------------
    if EntreName_Bis.get() != "":
        profil.append(EntreName_Bis.get())
    if EntreLast_Name_Bis.get() != "":
        profil.append(EntreLast_Name_Bis.get())
    if EntreNickname_Bis.get() != "":
        profil.append(EntreNickname_Bis.get())
    if len(EntreBirth_Bis.get()) == 8:
        profilYO['Birth_Bis']=EntreBirth_Bis.get()

    birth_mix(profilYO)
    for elements in profilYO.values():
        profilBirth.append(elements)
    return FinalMix(profil, profilBirth)


def birth_mix(x):
    if 'birth' in x.keys():

    	bdj = x['birth'][0:2]
    	x['jour'] = str(bdj)

    	bdm = x['birth'][2:4]
    	x['mois'] = str(bdm)

    	bdy_xxxx = x['birth'][4:9]
    	x['y_xxxx'] = str(bdy_xxxx)

    	bdy_xxx = x['birth'][5:9]
    	x['y_xxx'] = str(bdy_xxx)

    	bdy_xx = x['birth'][6:9]
    	x['y_xx'] = str(bdy_xx)

    "On s'occupe maintenant de la deuxieme partie (bis)"

    if 'Birth_Bis' in x.keys():

    	bdj_bis = x['Birth_Bis'][0:2]
    	x['jour_bis'] = str(bdj_bis)

    	bdm_bis = x['Birth_Bis'][2:4]
    	x['mois_bis'] = str(bdm_bis)

    	bdy_xxxx_bis = x['Birth_Bis'][4:9]
    	x['y_xxxx_bis'] = str(bdy_xxxx_bis)

    	bdy_xxx_bis = x['Birth_Bis'][5:9]
    	x['y_xxx_bis'] = str(bdy_xxx_bis)

    	bdy_xx_bis = x['Birth_Bis'][6:9]
    	x['y_xx_bis'] = str(bdy_xx_bis)

def FinalMix(profil, profilBirth):
    char = [
    r'#', '@', '%', '&',
    '*', '=', '_', '?'
    ]
    numb = ['0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9'
    ]
    with open("Nword.txt", 'w') as word: # On ouvre un fichier en mode ecriture

        "a 2"
        for a1 in profil:
            for b1 in profil + profilBirth:
                mix_a_2 = a1+b1                           # On creer un mix d'une addition de toutes les valeures
                mix_a_2_up = mix_a_2[0:].title()          # On met la premiere lettre en majuscule
                mix_a_2_maj = mix_a_2.upper()             # On met tout en majuscule
                word.write(f"{mix_a_2}\n")     # et on le met dans le fichier
                word.write(f"{mix_a_2_up}\n")
                word.write(f"{mix_a_2_maj}\n")
        "a 3"
        for a2 in profil:
            for b2 in profil + profilBirth:
                for c2 in profil + profilBirth:
                    mix_a_3 = a2+b2+c2                # Idem mais avec une addition de toutes les valeures 3 fois
                    mix_a_3_up = mix_a_3[0:].title()
                    mix_a_3_maj = mix_a_3.upper()
                    word.write(f"{mix_a_3}\n")
                    word.write(f"{mix_a_3_up}\n")
                    word.write(f"{mix_a_3_maj}\n")

        if addchar.get() == 1:
            "char simple"
            for a1 in profil:
                for b1 in char:
                    spe_char = a1+b1                # On associe a chaque valeures un char
                    spe_char_up = spe_char[0:].title()
                    spe_char_maj = spe_char.upper()
                    word.write(f"{spe_char}\n")
                    word.write(f"{spe_char_up}\n")
                    word.write(f"{spe_char_maj}\n")
            "char intermediaire"
            for a2 in char:
                for b2 in char:
                    char_mix = a2 + b2
                    for c2 in profil:
                        inter_mix = c2 + char_mix # On associe les char entre eux puis au valeures du profil
                        inter_mix_up = inter_mix[0:].title()
                        inter_mix_maj = inter_mix.upper()
                        word.write(f"{inter_mix}\n")
                        word.write(f"{inter_mix_up}\n")
                        word.write(f"{inter_mix_maj}\n")
            "char difficile"
            for a3 in char:
                for b3 in char:
                    char_mix1 = a3 + b3
                    for c3 in profil:
                        for d1 in profil + profilBirth:
                            val_mix = c3+d1
                            mix_ = val_mix + char_mix1
                            mix_0 = c3+a3+d1+b3
                            mix_1 = c3+a3+d1
                            mix_up = mix_[0:].title()
                            mix_0up = mix_0[0:].title()
                            mix_1up = mix_1[0:].title()
                            mix_maj = mix_.upper()
                            mix_0maj = mix_0.upper()
                            mix_1maj = mix_1.upper()
                            word.write(f"{mix_}\n")
                            word.write(f"{mix_0}\n")
                            word.write(f"{mix_1}\n")
                            word.write(f"{mix_up}\n")
                            word.write(f"{mix_0up}\n")
                            word.write(f"{mix_1up}\n")
                            word.write(f"{mix_maj}\n")
                            word.write(f"{mix_0maj}\n")
                            word.write(f"{mix_1maj}\n")
        if addnb.get() == 1:
            "numb simple"
            for e1 in profil:
                for f1 in numb:
                    spe_numb = a1+b1
                    spe_numb_up = spe_numb[0:].title()
                    spe_numb_maj = spe_numb.upper()
                    word.write(f"{spe_numb}\n")
                    word.write(f"{spe_numb_up}\n")
                    word.write(f"{spe_numb_maj}\n")
            "numb intermediaire"
            for e2 in numb:
                for f2 in numb:
                    numb_mix = e2 + f2
                    for g2 in profil:
                        inter_mix1 = g2 + numb_mix
                        inter_mix1_up = inter_mix1[0:].title()
                        inter_mix1_maj = inter_mix1.upper()
                        word.write(f"{inter_mix1}\n")
                        word.write(f"{inter_mix1_up}\n")
                        word.write(f"{inter_mix1_maj}\n")
            "numb difficile"
            for e3 in numb:
                for f3 in numb:
                    numb_mix1 = e3 + f3
                    for g3 in profil:
                        for h1 in profil + profilBirth:
                            val_mix1 = g3+h1
                            mix_2 = val_mix1 + numb_mix1
                            mix_3 = g3+e3+h1+f3
                            mix_4 = g3+e3+h1
                            mix_2up = mix_2[0:].title()
                            mix_3up = mix_3[0:].title()
                            mix_4up = mix_4[0:].title()
                            mix_2maj = mix_2.upper()
                            mix_3maj = mix_3.upper()
                            mix_4maj = mix_4.upper()
                            word.write(f"{mix_2}\n")
                            word.write(f"{mix_3}\n")
                            word.write(f"{mix_4}\n")
                            word.write(f"{mix_2up}\n")
                            word.write(f"{mix_3up}\n")
                            word.write(f"{mix_4up}\n")
                            word.write(f"{mix_2maj}\n")
                            word.write(f"{mix_3maj}\n")
                            word.write(f"{mix_4maj}\n")
    popup = Toplevel()
    popup.title('Success')
    popup.geometry('300x100')
    popup.resizable(width=FALSE, height=FALSE)
    finish = Label(popup, text="All data are stored in Nword.txt").pack()
    bouttonname = Button(popup, text='Finish', command=mafenetre.destroy).pack(padx=10, pady=10)


#Name 1
TexteName = Label(mafenetre, text='Name :', font=('Courrier', 15), bg="#4f83bb")
EntreName = Entry(mafenetre)
TexteName.place(x=25, y=25)
EntreName.place(x=25, y=55)

#Last_Name 1
TexteLast_Name = Label(mafenetre, text='Last Name :', font=('Courrier', 15), bg="#4f83bb")
EntreLast_Name = Entry(mafenetre)
TexteLast_Name.place(x=25, y=95)
EntreLast_Name.place(x=25, y=125)

#Surom 1
TexteNickname = Label(mafenetre, text='Nickname :', font=('Courrier', 15), bg="#4f83bb")
EntreNickname = Entry(mafenetre)
TexteNickname.place(x=25, y=155)
EntreNickname.place(x=25, y=185)

#Date de n'naissance 1
Textebirth = Label(mafenetre, text='BirthDay', font=('Courrier', 15), bg="#4f83bb")
Entrebirth = Entry(mafenetre)
Textebirth1 = Label(mafenetre, text='(ddmmyyyy)', font=('Courrier', 9), bg="#4f83bb")
Textebirth2 = Label(mafenetre, text=':', font=('Courrier', 15), bg="#4f83bb")

Textebirth.place(x=25, y=225)
Entrebirth.place(x=25, y=255)
Textebirth1.place(x=103, y=230)
Textebirth2.place(x=170, y=225)

#-------------------------------------------------------------------

#Name_Bis
TexteName_Bis = Label(mafenetre, text='Name_Bis :', font=('Courrier', 15), bg="#4f83bb")
EntreName_Bis = Entry(mafenetre)
TexteName_Bis.place(x=425, y=25)
EntreName_Bis.place(x=425, y=55)

#Last_Name_Bis
TexteLast_Name_Bis = Label(mafenetre, text='Last Name Bis :', font=('Courrier', 15), bg="#4f83bb")
EntreLast_Name_Bis = Entry(mafenetre)
TexteLast_Name_Bis.place(x=425, y=95)
EntreLast_Name_Bis.place(x=425, y=125)


#Surom_bis
TexteNickname_Bis = Label(mafenetre, text='Nickname_Bis :', font=('Courrier', 15), bg="#4f83bb")
EntreNickname_Bis = Entry(mafenetre)
TexteNickname_Bis.place(x=425, y=155)
EntreNickname_Bis.place(x=425, y=185)

#Date de n'naissance 2
TexteBirth_Bis = Label(mafenetre, text='BirthDay_Bis :', font=('Courrier', 15), bg="#4f83bb")
EntreBirth_Bis = Entry(mafenetre)
TexteBirth_Bis.place(x=425, y=225)
EntreBirth_Bis.place(x=425, y=255)

#-------------------------------------------------------------------

#Boutton de manip
addchar = IntVar()
CheckChar = Checkbutton(mafenetre, text="Special Char ?", variable=addchar)
CheckChar.place(x=253, y=290)
addnb= IntVar()
CheckNb = Checkbutton(mafenetre, text="Random Number ?", variable=addnb)
CheckNb.place(x=240, y=320)
MixBoutton = Button(mafenetre, text="Creer !", font=('Courrier', 15), command=entrer_dico)
MixBoutton.place(x=270, y=360)
QuitBoutton = Button(mafenetre, text="Exit", font=('Courrier', 15), padx=16, pady=0.40, command=mafenetre.destroy)
QuitBoutton.place(x=270, y=410)


mafenetre.mainloop()
