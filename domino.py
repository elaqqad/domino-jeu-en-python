from Tkinter import *
from random import randint
from classPile import *
from classDomino import *
from classJeumexicain import *
from classJoueur import *

################################################################################
## l'initialisation des fonctions et creation du jeu
################################################################################

jMexicain = JeuMexicain()
albert = Joueur(jMexicain.pioche)
mauricette = Joueur(jMexicain.pioche)
ginette = Joueur(jMexicain.pioche)
maurice = Joueur(jMexicain.pioche)
jMexicain.ajouterjoueur(albert)
jMexicain.ajouterjoueur(mauricette )
jMexicain.ajouterjoueur(ginette)
jMexicain.ajouterjoueur(maurice)
jMexicain.choisirjoueur()
partiefinie=False
gagnant=0

################################################################################
# La fonction principal du jeu 
################################################################################

def jouer() :
    if partiefinie() :
        donothing()
    else :
        jMexicain.jouer()
        afficherreserve()
        afficherTains()
        afficherdominodepart() 
        activationBottons()


################################################################################
# D'autres fonctions
################################################################################
# La fonction actvation desctivation des bottons  
def activationBottons():
    global jMexicain
    if jMexicain.joueuractuel==jMexicain.joueurs[0] :
        btn2['state']="active"
        btn3['state']="disabled"
        btn4['state']="disabled"
        btn5['state']="disabled"
    elif jMexicain.joueuractuel==jMexicain.joueurs[1] :
        btn2['state']="disabled"
        btn3['state']="active"
        btn4['state']="disabled"
        btn5['state']="disabled"
    elif jMexicain.joueuractuel==jMexicain.joueurs[2] :
        btn2['state']="disabled"
        btn3['state']="disabled"
        btn4['state']="active"
        btn5['state']="disabled"
    else:
        btn2['state']="disabled"
        btn3['state']="disabled"
        btn4['state']="disabled"
        btn5['state']="active"
    
 
# la fonction qui affiche la reserve de maurice   
def afficherreserve():
    global photoR,maurice
    for i in range(1,4):
        for j in range(5):
            if (i-1)*5+j < len(maurice.reserve):
                photoR[i-1][j]=PhotoImage(file='image\\petit-'+str(maurice.reserve[(i-1)*5+j].A) +'-'+str(maurice.reserve[(i-1)*5+j].B)+'.gif')
            else:
                photoR[i-1][j]=PhotoImage(file="image\\petit--1--1.gif")
    for i in range(3) :
        for j in range(5) :
            reserve.create_image(20+80*j,10+50*i, image=photoR[i][j],anchor=NW) 



# La fonction qui permet d'afficher les trains des joueurs et le train Mexicain  
def afficherTains():
    global photo,jMexecain
    for i in range(1,6) :
        if i!=1   :
            l=min(5,jMexicain.joueurs[i-2].train.taille())
            for j in range(l):
                dom=jMexicain.joueurs[i-2].train.lesElts[jMexicain.joueurs[i-2].train.taille()-l+j]
                photo[i-1][j]=PhotoImage(file='image\\petit-'+str(dom.A) +'-'+str(dom.B)+'.gif')       
        else :
            l=min(5,jMexicain.trainM.taille()) 
            for j in range(l):
                dom=jMexicain.trainM.lesElts[jMexicain.trainM.nb-l+j]
                photo[i-1][j]=PhotoImage(file='image\\petit-'+str(dom.A) +'-'+str(dom.B)+'.gif')              
    for i in range(5) :
        for j in range(5) :
            trains.create_image(20+80*j,10+50*i, image=photo[i][j],anchor=NW)    


# La fonction qui permet l'affichage de domino de depart
def afficherdominodepart() :
    global photoD,jMexecain
    dom=jMexicain.dominoDepart
    photoD=PhotoImage(file='image\\petit-'+str(dom.A) +'-'+str(dom.B)+'.gif') 
    dominodepart.create_image(20,10, image=photoD,anchor=NW)     


# La fonction qui ouvre la fenetre de in de jeu
def donothing():
    filewin = Toplevel(fen)
    chaine='La partie est terminée, le gaganat est : \n\n'+nomdejoueur(gagnant)
    butt = Button(filewin, text=chaine)
    but=Button(filewin,text='quitter',command=fen.quit)
    butt.pack()
    but.pack()
    
 
 
 # La fonction indicatrice de la fin de la partie   
def partiefinie() :
    global gagnant
    for j in jMexicain.joueurs :
        if j.nombreDominosReserve == 0 :
            gangnant=j
    if jMexicain.piocheVide() :
        gagnant=jMexicain.joueurs[0]
        for j in jMexicain.joueurs :
            if j.valeurReserve() <gagnant.valeurReserve() :
                gangnant=j
    if gagnant!=0 :
        return True
    return False

# la fonction qui retourne le nom de joueur
def nomdejoueur(j) :
    if j==albert :
        return 'albert'
    elif j==mauricette:
        return 'mauricette'
    elif j==ginette :
        return 'ginette'
    else  :
        return 'maurice'


################################################################################
# La construction des frames dt des canvas et...
################################################################################

# Fenetre principale
fen = Tk()
fen.title('Jeu de dominos')
fen.geometry("800x570")


# l'initialisation des images des domino ou domino vide
i=1
photo=[] # les mages sur les trains
for i in range(5) :
    photos=[]
    for j in range(5) :
        photos.append(PhotoImage(file="image\\petit--1--1.gif"))
    photo.append(photos)
photoR=[] # les images de la reserve
for i in range(3) :
    photos=[]
    for j in range(5) :
        photos.append(PhotoImage(file="image\\petit--1--1.gif"))
    photoR.append(photos)
photoD=PhotoImage(file="image\\petit-1-1.gif") # l'image domino de depert


# frame 1 :reserve, domino de depart
frm2=Frame(fen)
lbl11= Label(frm2, text='Domino de')
lbl12 = Label(frm2, text='depard')
lbl22=Label(frm2, text='reserve de maurice')
reserve=Canvas(frm2,width=420, height=150,bg='green')
dominodepart=Canvas(frm2,width=95, height=50,bg='green')
lbl11.grid(row=1,column=1)
lbl12.grid(row=2,column=1)
lbl22.grid(row=4,column=1,columnspan=2)
dominodepart.grid(row=3,column=1,rowspan=1,padx=5,pady=5)
reserve.grid(row=1,column=2,rowspan=3,padx=5,pady=5)
frm2.pack(side=TOP)



# frame 2 : Les trains des joueurs , les noms des joueurs , les boutons
frm1=Frame(fen)
trains=Canvas(frm1,width=420, height=250,bg='black')
trains.grid(row=1,column=3,rowspan=5,padx=5,pady=5)
frm1.pack(side=TOP)


btn1 = Button(frm1, width=6, height=1, text='Tr.mex',command=jouer)
btn2 = Button(frm1, width=6, height=1, text='albert',command=jouer)
btn3 = Button(frm1, width=6, height=1, text='mette ',command=jouer)
btn4 = Button(frm1, width=6, height=1, text='gine  ',command=jouer)
btn5 = Button(frm1, width=6, height=1, text='maur  ',command=jouer)
lbl1 = Label(frm1, text='TrM')
lbl2 = Label(frm1, text='Alb')
lbl3 = Label(frm1, text='Mtt')
lbl4 = Label(frm1, text='Gin')
lbl5 = Label(frm1, text='Mau')

btn1.grid(row=1,column=1)
btn2.grid(row=2,column=1)
btn3.grid(row=3,column=1)
btn4.grid(row=4,column=1)
btn5.grid(row=5,column=1)
lbl1.grid(row=1,column=2)
lbl2.grid(row=2,column=2)
lbl3.grid(row=3,column=2)
lbl4.grid(row=4,column=2)
lbl5.grid(row=5,column=2)



# initialisation
btn1['state']="disabled"
afficherreserve()
afficherTains()
afficherdominodepart()
activationBottons()

# lancer la fenetre

fen.mainloop()
fen.destroy()