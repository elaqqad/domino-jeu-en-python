from random import randint
from classPile import *
from classDomino import *

class JeuMexicain:

        def __init__(self):
                ''' JeuMexicain -> JeuMexicain
                Construit la classe. '''
                self.dominoDepart = Domino(-1, -1)
                self.trainM= Pile()
                self.pioche = []
                for i in range(0, 13):
                    for j in range(i, 13):
                        self.pioche.append(Domino(i, j))
                self.joueurs = []
                self.joueuractuel=0

        def ajouterjoueur(self,joueur) :
                self.joueurs.append(joueur)
                
        def joueursuivant(self) :
                i=0
                while self.joueuractuel!=self.joueurs[i]:
                        i=i+1
                self.joueuractuel=self.joueurs[(i+1) % len(self.joueurs)]
        def joueurprecedent(self) :
                i=0
                while self.joueuractuel!=self.joueurs[i]:
                        i=i+1
                return self.joueurs[(i-1) % len(self.joueurs)]        
        
        def choisirjoueur(self):
                import random
                self.joueuractuel=random.choice(self.joueurs)

        def piocheVide(self):
                ''' JeuMexicain -> bool
                Teste si la pioche est vide. '''
                return len(self.pioche) == 0

        def jouer(self) :
                if self.dominoDepart.estVide():
                        d=self.joueuractuel.plusGrandDominoDouble()
                        if not d.estVide() :
                                self.dominoDepart=d
                                self.joueuractuel.reserve.remove(d)
                        else:
                                self.joueuractuel.piocherDomino(self.pioche)
                                self.joueursuivant()
                                
                else:
                        d=self.joueuractuel.premierDominoSurLeT(self.dominoDepart)
                        if not d.estVide() :
                                self.joueuractuel.train.empiler(d)
                                self.joueuractuel.reserve.remove(d)
                                if not d.estDouble():
                                        self.joueursuivant()                                
                        else :
                                d=self.joueuractuel.premierDominoSurLeTM(self.dominoDepart,self.trainM)
                                if  not d.estVide() :
                                        self.trainM.empiler(d)
                                        self.joueuractuel.reserve.remove(d)
                                        if not d.estDouble():
                                                self.joueursuivant()                                        
                                else :
                                        self.joueuractuel.piocherDomino(self.pioche)
                                        self.joueursuivant()
                                        
                                        
        def jouersimple(self) :
                if self.dominoDepart.estVide():
                        d=self.joueuractuel.plusGrandDominoDouble()
                        if not d.estVide() :
                                self.dominoDepart=d
                                self.joueuractuel.reserve.remove(d)
                        else:
                                self.joueuractuel.piocherDomino(self.pioche)
                                self.joueursuivant()
                                
                else:
                        d=self.joueuractuel.premierDominoSurLeT(self.dominoDepart)
                        if not d.estVide() :
                                self.joueuractuel.train.empiler(d)
                                self.joueuractuel.reserve.remove(d)
                                if not d.estDouble():
                                        self.joueursuivant()                                
                        else :

                                self.joueuractuel.piocherDomino(self.pioche)
                                self.joueursuivant()                





