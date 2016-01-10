from classJeumexicain import *
from classPile import *
from classDomino import *

class Joueur:

    def __init__(self,pioche):
        ''' Joueur -> Joueur
        Construit la classe Joueur. '''
        self.train = Pile()
        self.reserve = []
        for i in range(10) :
            self.piocherDomino(pioche)

    def plusGrandDominoDouble(self):
        ''' Joueur -> Domino
        Retourne la valeur du plus grand domino double dans la reserve du joueur. '''
        DominoDouble = Domino(-1, -1)
        for dom in self.reserve:
            if dom.estDouble() and dom.estPlusGrand(DominoDouble):
                DominoDouble=dom
        return DominoDouble


    def premierDominoSurLeT(self,dominodepart):
        ''' Joueur -> Domino
        Retourne le premier domino de la reserve qui peut etre pose sur le train du joueur. '''
        if self.train.taille()!=0:
            dernDom=self.train.sommet()
        else:
            dernDom=dominodepart
        for dom in self.reserve:
            if dom.A == dernDom.B:
                return dom
            elif dom.B == dernDom.B:
                dom.permute()
                return dom
        return Domino(-1, -1)
    
    def premierDominoSurLeTM(self,dominodepart,trainM):
        ''' Joueur -> Domino
        Retourne le premier domino de la reserve qui peut etre pose sur le trainM. '''
        if trainM.taille()!=0:
            dernDom=trainM.sommet()
        else:
            dernDom=dominodepart
        for dom in self.reserve:
            if dom.A == dernDom.B:
                return dom
            elif dom.B == dernDom.B:
                dom.permute()
                return dom
        return Domino(-1, -1)

    def nombreDominosReserve(self):
        ''' Joueur -> int
        Retourne le nombre de dominos dans la reserve du joueur. '''
        return len(self.reserve)
    def valeurReserve(self) :
        v=0
        for dom in self.reserve :
            v=v+dom.valeur()
        return v
    
    
    def piocherDomino(self,pioche):
        ind = randint(0, len(pioche)-1)
        dom=pioche.pop(ind)        
        self.reserve.append(dom)