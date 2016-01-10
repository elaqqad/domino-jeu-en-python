class Pile :
        '''Definition d'une pile'''

        def __init__(self):
                ''' -> Pile
                Cree une pile'''
                self.lesElts=[]
                self.nb=0

        def empiler(self,elt):
                '''Pile, Objet -> Rien
                Empile un objet au sommet de la pile'''
                if len(self.lesElts) == self.nb:
                        self.lesElts.append(elt)
                else :
                        self.lesElts[self.nb] = elt
                self.nb += 1

        def depiler(self):
                '''Pile -> Objet
                Retourne l'objet au sommet de la pile et l'enleve'''
                assert not self.estVide()
                elt=self.lesElts[self.nb-1]
                del self.lesElts[self.nb-1]
                self.nb-=1
                return elt

        def estVide(self):
                '''Pile -> Bool
                Teste si la pile est vide'''
                return self.nb==0

        def sommet(self):
                '''Pile -> Objet
                Retourne l'objet qui se trouve au sommet de la pile'''
                assert not self.estVide()
                return self.lesElts[self.nb-1]

        def taille(self):
                '''Pile -> int
                Retourne la taille de la pile.'''
                return self.nb
