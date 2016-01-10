class Domino:
        ''' Permet d'instancier des objets simulant les pieces d'un jeu de dominos. '''

        def __init__(self, A, B):
                ''' Domino, int, int -> Domino
                Initialise les valeurs des points presents sur les deux faces du domino. '''
                self.A = A
                self.B = B

        def str(self):
                ''' Domino -> rien
                Affiche les points presents sur les deux faces. '''
                return '['+str(self.A)+' | '+str(self.B)+']'

        def valeur(self):
                ''' Domino -> int
                Affiche la somme des points presents sur les deux faces. '''
                return self.A + self.B

        def estDouble(self):
                ''' Domino -> bool
                Teste si un domino est double. '''
                return self.A == self.B
        def estVide(self):
                ''' Domino -> bool
                Teste si un domino est vide. '''
                return self.egal(Domino(-1,-1))
        def peutEtrePlaceApres(self, domino):
                ''' Domino, Domino -> bool
                Teste si le domino courant peut etre place apres domino. '''
                return (self.B == domino.A or self.B == domino.B)

        def permute(self):
                ''' Domino -> Domino
                Permet d'inverser les deux faces d'un domino. '''
                self.A, self.B = self.B, self.A

        def egal(self, domino):
                ''' Domino, Domino -> bool
                Teste si deux dominos sont egaux. '''
                if (self.A == domino.A and self.B == domino.B) or (self.A == domino.B and self.B == domino.A):
                        return True
                return False

        def estPlusGrand(self, dom):
                '''Domino, Domino -> Bool
                Teste si un domino est plus grand qu'un autre domino.'''
                return self.valeur() > dom.valeur()

#d1 = Domino(2, 12)
#d2 = Domino(12, 2)
#d3 = Domino(3, 4)
#print(d1.str())
#d1.permute()
#print(d1.str())
#print(d1.egal(d2))
#print(d1.estPlusGrand(d2))
#print(d1.estPlusGrand(d3))

